import os
import shutil
import errno
import glob
from django.conf import settings
from zipfile import ZipFile

from spl.models import Task
from spl.ftp import PillboxFTP


class DownloadAndUnzip(object):

    def __init__(self, task_id, source_title, files, host, ftp_path):
        """
        @param
        task_id - The id of the task created in the task model of spl
        source - the name of the SPL source e.g. HOTC
        files - the list of files associated with the source e.g. dm_spl_release_animal.zip
        """
        self.task = Task.objects.get(pk=task_id)
        self.source = source_title
        self.files = files
        self.host = host
        self.ftp_path = ftp_path

    def run(self):

        self.task.pid = os.getpid()
        self.task.save()

        if self.download():
            if self.unzip():
                return True
        return False

    def download(self):
        # Making necessary folders
        path = check_create_folder(settings.DOWNLOAD_PATH)
        path = check_create_folder(path + '/' + self.source)

        self.task.status = 'PROGRESS: DOWNLOAD'
        self.task.save()

        # Download all files
        for f in self.files:
            ftp = PillboxFTP(self.host,
                             settings.DAILYMED_FTP_USER,
                             settings.DAILYMED_FTP_PASS,
                             self.task.id)
            ftp.download(self.ftp_path, f, path)

        return True

    def unzip(self):

        percent = 0.0

        self.task = Task.objects.get(pk=self.task.id)
        self.task.status = 'PROGRESS: UNZIP'
        meta = {
            'action': 'unzip',
            'file': 'Unzip %s' % self.source,
            'percent': percent,
            'items_unzipped': 0
        }
        self.task.meta.update(meta)
        self.task.save()

        zip_path = settings.DOWNLOAD_PATH
        unzip_path = settings.SOURCE_PATH

        final_path = check_create_folder('%s/%s' % (unzip_path, self.source))
        tmp_path = check_create_folder('%s/%s/tmp' % (unzip_path, self.source))
        tmp_path2 = check_create_folder('%s/%s/tmp2' % (unzip_path, self.source))
        total_weight = len(self.files)

        for zipped in self.files:
            #Initial Unzip Round
            # operation weigth 30%
            weight = 0.3

            zip = ZipFile('%s/%s/%s' % (zip_path, self.source, zipped), 'r')
            zip.extractall(path=tmp_path)
            zip.close()
            percent += (weight/total_weight) * 100
            self.task.meta['percent'] = percent
            self.task.save()

            # Second round of unzipping of files inside the unzip file
            # operation weight 70%
            weight = 0.7
            new_zip_files = glob.glob(tmp_path + '/*/*.zip')
            total_files = len(new_zip_files)
            file_counter = 0
            for zipped in new_zip_files:
                file_counter += 1

                zip = ZipFile(zipped, 'r')
                zip.extractall(path=tmp_path2)
                zip.close()
                percent += (file_counter / total_files) * ((weight/total_weight) * 100)
                if file_counter % 20 == 0:
                    self.task.meta['items_unzipped'] = file_counter
                    self.task.meta['percent'] = percent
                    self.task.save()

        # copy xml files to the correct place
        unzipped_files = glob.glob(tmp_path2 + '/*.xml')
        for item in unzipped_files:
            shutil.copy(item, final_path)

        # delete tmp files
        try:
            shutil.rmtree(tmp_path)
            # shutil.rmtree(tmp_path2)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise

        self.task.meta['percent'] = 100
        self.task.save()
        return True


def check_create_folder(folder_path):
    """ Check whether a folder exists, if not the folder is created
    Always return folder_path
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path
