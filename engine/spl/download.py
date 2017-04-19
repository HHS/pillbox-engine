from __future__ import division
import os
import shutil
import errno
import glob
from django.conf import settings
from django.utils import timezone
from zipfile import ZipFile

from spl.models import Task, Source
from spl.ftp import PillboxFTP


class DownloadAndUnzip(object):

    def __init__(self, task_id, source_id):
        """
        @param
        task_id - The id of the task created in the task model of spl
        source - the name of the SPL source e.g. HOTC
        files - the list of files associated with the source e.g. dm_spl_release_animal.zip
        """
        self.task = Task.objects.get(pk=task_id)
        self.source = Source.objects.get(pk=source_id)
        self.files = self.source.files
        self.host = self.source.host
        self.ftp_path = self.source.path

    def run(self):

        self.task.pid = os.getpid()
        self.task.save()

        if self.download():
            return self.unzip()

    def download(self):
        # Making necessary folders
        path = check_create_folder(settings.DOWNLOAD_PATH)
        path = check_create_folder(path + '/' + self.source.title)

        self.task.status = 'PROGRESS: DOWNLOAD'
        self.task.save()

        # Download all files
        for f in self.files:
            ftp = PillboxFTP(self.host,
                             settings.DAILYMED_FTP_USER,
                             settings.DAILYMED_FTP_PASS,
                             self.task.id)
            ftp.download(self.ftp_path, f, path)

        self.source.last_downloaded = timezone.now()
        self.source.save()

        return True

    def _unzipWithProgress(self, src, dst, weight = 100, percent=0):
        zp = ZipFile(src, 'r')
        total_files = len(zp.infolist())

        # provider percentage only if there are more than 1000 files to unzip
        if total_files >= 1000:
            print('There are %s files to unzip in %s' % (total_files, src))


            count = 0
            for file in zp.infolist():
                zp.extract(file, path=dst)
                count += 1
                if round(count) % 1000 == 0.0:
                    new_percent = percent + (count / total_files * weight)
                    self.task.meta['percent'] = float('{0:.2f}'.format(new_percent))
                    self.task.save()
        else:
            zp.extractall(path=dst)
        zp.close()
        print('Successfully unzipped all files in %s' % src)
        return percent + weight

    def unzip(self):
        percent = 0

        self.task = Task.objects.get(pk=self.task.id)
        self.task.status = 'PROGRESS: UNZIP'
        meta = {
            'action': 'unzip',
            'file': 'Unzip %s' % self.source.title,
            'percent': percent,
            'items_unzipped': 0
        }
        self.task.meta.update(meta)
        self.task.save()

        zip_path = settings.DOWNLOAD_PATH
        unzip_path = settings.SOURCE_PATH

        final_path = check_create_folder('%s/%s' % (unzip_path, self.source.title))
        total_weight = len(self.files)

        file_counter = 0
        tmp_number = 0
        for zipped in self.files:
            self.task.meta['file'] = 'Unzipping %s' % zipped
            self.task.save()

            tmp_path = check_create_folder('%s/%s/tmp' % (unzip_path, self.source.title))
            tmp_path2 = check_create_folder('%s/%s/tmp2' % (unzip_path, self.source.title))
            weight = 0.5 / total_weight * 100

            self._unzipWithProgress(
                '%s/%s/%s' % (zip_path, self.source.title, zipped),
                tmp_path,
                weight,
                percent
            )

            percent = percent + weight
            self.task.meta['percent'] = percent
            self.task.save()

            weight = 0.5 / total_weight * 100
            new_zip_files = glob.glob(tmp_path + '/*/*.zip')
            total_files = len(new_zip_files)

            counter = 0

            for zipped in new_zip_files:
                counter += 1
                self._unzipWithProgress(zipped, tmp_path2)
                if round(counter) % 300 == 0.0:
                    new_percent = percent + (counter / total_files * weight)
                    self.task.meta['percent'] = float('{0:.2f}'.format(new_percent))
                    self.task.save()

            file_counter += counter

            percent = percent + weight
            self.task.meta['percent'] = percent
            self.task.meta['items_unzipped'] = file_counter
            self.task.save()

            # delete tmp files
            try:
                shutil.rmtree(tmp_path, ignore_errors=True)
            except OSError as exc:
                if exc.errno != errno.ENOENT:
                    raise

            tmp_number += 1

        # copy xml files to the correct place
        self.task.meta['file'] = 'Copying files to final place'
        self.task.save()

        unzipped_files = glob.glob(tmp_path2 + '/*.xml')
        print('Copying files to final location')
        for item in unzipped_files:
            shutil.copy(item, final_path)

        self.task.meta['percent'] = 100
        self.task.meta['items_unzipped'] = file_counter
        self.task.save()

        self.source.last_unzipped = timezone.now()
        self.source.save()
        return True


def check_create_folder(folder_path):
    """ Check whether a folder exists, if not the folder is created
    Always return folder_path
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path
