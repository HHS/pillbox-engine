from __future__ import absolute_import, division
import time
import os
import glob
import errno
import shutil
from zipfile import ZipFile
from django.conf import settings
from django.utils import timezone

from _celery import app
from spl.sync.controller import Controller
from spl.ftp import PillboxFTP
from spl.models import Download


@app.task()
def add(x, y):
    print '%s' % (x + y)


@app.task(bind=True, ignore_result=True)
def sync(self, action):

    arguments = ['products', 'pills', 'all']

    if action in arguments:
        controller = Controller(celery=self)
        controller.sync(action)


@app.task(bind=True, ignore_result=True)
def download_task(self, download_id, download_type, files):
    start = time.time()

    path = check_create_folder(settings.DOWNLOAD_PATH)

    # Make a separate folder for the type
    path = check_create_folder(path + '/' + download_type)

    self.update_state(state='STARTED')

    success = True
    for f in files:
        ftp = PillboxFTP(settings.DAILYMED_FTP_SITE,
                         settings.DAILYMED_FTP_USER,
                         settings.DAILYMED_FTP_PASS,
                         self.request.id)
        state = ftp.download(settings.DAILYMED_FTP_PATH, f, path)

    end = time.time()
    spent = end - start

    if success:
        download_obj = Download.objects.get(id=download_id)
        setattr(download_obj, download_type, True)
        download_obj.duration += spent
        download_obj.status = 'DOWNLOAD'
        download_obj.save()

    return True


@app.task(bind=True, ignore_result=True)
def unzip_task(self, download_id):

    start = time.time()

    zip_path = settings.DOWNLOAD_PATH
    unzip_path = settings.SOURCE_PATH
    files = settings.DAILYMED_FILES

    counter = {
        'sources': 0,
        'files': 0,
    }

    total = len(files.keys())

    for folder, zip_files in files.iteritems():
        folder = folder.upper()
        counter['sources'] += 1

        self.update_state(state='PROGRESS',
                          meta={
                                'action': 'unzip',
                                'sources': counter['sources'],
                                'files': counter['files'],
                                'percent': round((counter['sources'] / total) * 100, 2)
                          })

        final_path = check_create_folder('%s/%s' % (unzip_path, folder))
        tmp_path = check_create_folder('%s/%s/tmp' % (unzip_path, folder))
        tmp_path2 = check_create_folder('%s/%s/tmp2' % (unzip_path, folder))
        for zipped in zip_files:
            #Initial Unzip Round
            zip = ZipFile('%s/%s/%s' % (zip_path, folder, zipped), 'r')
            zip.extractall(path=tmp_path)
            zip.close()

            # Second round of unzipping of files inside the unzip file
            new_zip_files = glob.glob(tmp_path + '/%s/*.zip' % zipped.replace('.zip', ''))
            for zipped in new_zip_files:
                counter['files'] += 1
                zip = ZipFile(zipped, 'r')
                zip.extractall(path=tmp_path2)
                zip.close()

        # copy xml files to the correct place
        unzipped_files = glob.glob(tmp_path2 + '/*.xml')
        for item in unzipped_files:
            shutil.copy(item, final_path)

        # delete tmp files
        try:
            shutil.rmtree(tmp_path)
            shutil.rmtree(tmp_path2)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise

    end = time.time()
    spent = end - start

    download_obj = Download.objects.get(id=download_id)
    download_obj.unzipped = True
    download_obj.completed = True
    download_obj.ended = timezone.now()
    download_obj.duration += spent
    download_obj.status = 'SUCCESS'
    download_obj.save()

    self.update_state(state='SUCCESS')


def check_create_folder(folder_path):
    """ Check whether a folder exists, if not the folder is created
    Always return folder_path
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path
