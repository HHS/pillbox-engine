from __future__ import print_function
"""
The MIT License (MIT)

Copyright (c) 2013 keepitsimple

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

source: https://github.com/keepitsimple/pyFTPclient
"""
__author__ = 'Roman Podlinov'


import sys
import threading
import logging
import ftplib
import socket
import time

try:
    from djcelery_pillbox.models import TaskMeta
    from django.conf import settings
except ImportError:
    pass

def setInterval(interval, times=-1):
    # This will be the actual decorator,
    # with fixed interval and times parameter
    def outer_wrap(function):
        # This will be the function to be
        # called
        def wrap(*args, **kwargs):
            stop = threading.Event()

            # This is another function to be executed
            # in a different thread to simulate setInterval
            def inner_wrap():
                i = 0
                while i != times and not stop.isSet():
                    stop.wait(interval)
                    function(*args, **kwargs)
                    i += 1

            t = threading.Timer(0, inner_wrap)
            t.daemon = True
            t.start()
            return stop
        return wrap
    return outer_wrap


class PyFTPclient(object):

    def __init__(self, host, port, login, passwd, monitor_interval=30, task_id=None):
        self.host = host
        self.port = port
        self.login = login
        self.passwd = passwd
        self.monitor_interval = monitor_interval
        self.ptr = None
        self.max_attempts = 15
        self.waiting = True
        self.task_id = task_id

    def set_state(self, state, meta=None):
        """ Updates Celery's taskmeta with a new state """
        if self.task_id:
            try:
                task = TaskMeta.objects.get(task_id=self.task_id)
                if task.status != 'SUCCESS':
                    task.status = state
                    if meta:
                        task.meta = meta
                    task.save()
            except TaskMeta.DoesNotExist:
                pass
        else:
            print("%d  -  %0.1f Kb/s" % (meta['downloaded'], meta['speed']), end='\r')
            sys.stdout.flush()

    def download_file(self, dst_filename, local_filename=None):
        res = ''
        if local_filename is None:
            local_filename = dst_filename

        with open(local_filename, 'w+b') as f:
            self.ptr = f.tell()

            @setInterval(self.monitor_interval)
            def monitor():
                if not self.waiting:
                    try:
                        i = f.tell()
                        if self.ptr < i:
                            speed = (i-self.ptr)/(1024*self.monitor_interval)
                            meta = {
                                'downloaded': i,
                                'speed': speed,
                                'action': 'download',
                                'file': dst_filename,
                                'size': dst_filesize
                            }
                            self.set_state('PROGESS', meta)
                            self.ptr = i
                        else:
                            ftp.close()
                    except ValueError:
                        # If the download was completed just pass
                        pass

            def connect():
                ftp.connect(self.host, self.port)
                ftp.login(self.login, self.passwd)
                # optimize socket params for download task
                ftp.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                ftp.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 75)
                # ftp.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)

            ftp = ftplib.FTP()
            ftp.set_debuglevel(2)
            ftp.set_pasv(True)

            connect()
            ftp.voidcmd('TYPE I')
            dst_filesize = ftp.size(dst_filename)

            mon = monitor()
            while dst_filesize > f.tell():
                try:
                    connect()
                    self.waiting = False
                    # retrieve file from position where we were disconnected
                    res = (ftp.retrbinary('RETR %s' % dst_filename, f.write) if f.tell() == 0 else
                           ftp.retrbinary('RETR %s' % dst_filename, f.write, rest=f.tell()))

                except:
                    self.max_attempts -= 1
                    if self.max_attempts == 0:
                        mon.set()
                        logging.exception('')
                        raise
                    self.waiting = True
                    logging.info('waiting 30 sec...')
                    time.sleep(30)
                    logging.info('reconnect')

            mon.set()  # stop monitor
            ftp.close()

            if not res.startswith('226 Transfer complete'):
                logging.error('Downloaded file {0} is not full.'.format(dst_filename))
                # self.set_state('FAILURE')
                return False
            self.set_state('SUCCESS')
            return True


if __name__ == "__main__":
    obj = PyFTPclient('54.225.98.204', 21, 'saaadftp', 'oT2tVfyGXNDawLB4Mxq', 1)
    obj.download_file('pbs/zip/dm_spl_release_human_rx_part1.zip', 'test.zip')
