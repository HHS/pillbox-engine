from __future__ import print_function, division

import ftputil
from djcelery_pillbox.models import TaskMeta


class PillboxFTP(object):
    """ This is pillbox's FTP class for downloading large DailyMed files
    from NIH FTP server """

    def __init__(self, host, username, password, task_id=None, port=None):
        self.ftp = ftputil.FTPHost(host, username, password)
        self.file_size = 0
        self.received = 0
        self.task_id = task_id
        self.filename = None

    def progress(self, chunk):
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

        if self.task_id:
            task = TaskMeta.objects.get(task_id=self.task_id)
            task.status = 'PROGRESS'
            task.meta = meta
            task.save()
        else:
            print(meta)

    def success(self):
        if self.task_id:
            task = TaskMeta.objects.get(task_id=self.task_id)
            task.status = 'SUCCESS'
            task.save()

    def download(self, src_path, filename, dst_path):
        """ Download the file if it is newer """
        #Get file size
        self.file_size = self.ftp.path.getsize(src_path + '/' + filename)
        self.filename = filename

        state = self.ftp.download_if_newer(src_path + '/' + filename,
                                           dst_path + '/' + filename,
                                           callback=self.progress)
        self.success()
        return state
