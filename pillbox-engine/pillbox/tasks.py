from __future__ import absolute_import

from _celery import app

from pillbox.importer import importer


@app.task(bind=True, ignore_result=True)
def import_task(self, csv_file, import_id):

    importer(csv_file, import_id, self)
