from __future__ import absolute_import

from _celery import app

from spl.sync.controller import Controller


@app.task(bind=True)
def sync(self, action):

    arguments = ['products', 'pills', 'all']

    if action in arguments:
        controller = Controller(celery=self)
        controller.sync(action)
