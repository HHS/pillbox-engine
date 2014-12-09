from __future__ import print_function, division
import os
import time
import ftputil
from spl.models import Task


class PillboxFTP(object):
    """ This is pillbox's FTP class for downloading large DailyMed files
    from NIH FTP server """

    def __init__(self, host, username, password, task_id=None, port=None):
        self.start = time.time()
        self.ftp = ftputil.FTPHost(host, username, password)
        self.file_size = 0
        self.received = 0
        self.update_interval = 0
        try:
            self.task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            self.task = None
        self.filename = None

    def progress(self, chunk=''):
        """ A callback function that receives chunk info from ftp downloader
        and calculates progress
        """
        self.received += len(chunk)
        percent = round((self.received / self.file_size) * 100, 2)

        ## Keep ftp connection alive
        ## read more here: http://ftputil.sschwarzer.net/trac/wiki/Documentation#ftphost-instances-vs-ftp-connections
        now = time.time()
        if ((now - self.start) > 100):
            self.start = time.time()
            # self.ftp.chdir(self.ftp.getcwd())
            self.ftp.listdir(self.ftp.curdir)

            print('keeping the ftp connection alive')

        ## To decrease the number of times the database is called, update meta data
        ## in integer intervals
        if int(percent) > self.update_interval:
            self.update_interval = int(percent)
            meta = {
                'downloaded': self.received,
                'action': 'download',
                'file': self.filename,
                'size': self.file_size,
                'percent': percent
            }

            if self.task:
                self.task.meta.update(meta)
                self.task.save()
                # print(meta)
            else:
                print(meta)

    def download(self, src_path, filename, dst_path):
        """ Download the file if it is newer """
        #Get file size

        self.file_size = self.ftp.path.getsize(src_path + '/' + filename)
        self.compare_files(filename, dst_path)
        self.filename = filename

        state = self.ftp.download_if_newer(src_path + '/' + filename,
                                           dst_path + '/' + filename,
                                           callback=self.progress)

        self.ftp.close()
        return state

    def compare_files(self, filename, dst_path):
        """ Compare if the file already donwloaded and if it is the same size
        This is important because with download_if_newer method ftputil skip files that
        were partially downloaded
        """
        try:
            local_size = os.path.getsize(dst_path + '/' + filename)

            if local_size != self.file_size:
                os.remove(dst_path + '/' + filename)
                print('%s deleted' % filename)
        except OSError:
            pass
