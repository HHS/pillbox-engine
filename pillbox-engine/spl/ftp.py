from __future__ import print_function, division

import ftputil
from spl.models import Task


class PillboxFTP(object):
    """ This is pillbox's FTP class for downloading large DailyMed files
    from NIH FTP server """

    def __init__(self, host, username, password, task_id=None, port=None):
        self.ftp = ftputil.FTPHost(host, username, password)
        self.file_size = 0
        self.received = 0
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
        meta = {
            'downloaded': self.received,
            'action': 'download',
            'file': self.filename,
            'size': self.file_size,
            'percent': percent
        }

        self.ftp.keep_alive()

        if self.task:
            self.task.meta = meta
            self.task.save()
        else:
            print(meta)

    def download(self, src_path, filename, dst_path):
        """ Download the file if it is newer """
        #Get file size
        self.file_size = self.ftp.path.getsize(src_path + '/' + filename)
        self.filename = filename

        self.progress()

        state = self.ftp.download_if_newer(src_path + '/' + filename,
                                           dst_path + '/' + filename,
                                           callback=self.progress)
        return state
