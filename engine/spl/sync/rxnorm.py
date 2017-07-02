from __future__ import division

import sys
import threading
import requests
import simplejson as json
from django.utils import timezone

from spl.models import Pill, Task

def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


class SignalHandler:
    """
    The object that will handle signals and stop the worker threads.
    """

    #: The stop event that's shared by this handler and threads.
    stopper = None

    #: The pool of worker threads
    workers = None

    def __init__(self, stopper, workers):
        self.stopper = stopper
        self.workers = workers

    def __call__(self, signum, frame):
        """
        This will be called by the python signal module

        https://docs.python.org/3/library/signal.html#signal.signal
        """
        print('received ctrl+c. Stopping threads')
        self.stopper.set()

        for worker in self.workers:
            worker.join()

        sys.exit(0)


class ThreadXNorm(threading.Thread):
    def __init__(self, queue, stopper, task_id=None):
        threading.Thread.__init__(self)
        self.queue = queue
        self.task_id = task_id
        self.stopper = stopper

    def run(self):
        while True:
            if self.stopper.is_set():
                break

            #grabs file from queue
            pill_id = self.queue.get()

            try:
                pill = Pill.objects.get(pk=pill_id)

                message('Processing pill: %s' % pill.product_code)
                rx = rxnorm(pill.product_code)

                pill.rxstring = rx['rxstring']
                pill.rxtty = rx['rxtty']
                pill.rxcui = rx['rxcui']
                pill.rx_update_time = timezone.now()
                pill.save()

                if self.task_id:
                    task = Task.objects.get(pk=self.task_id)

                    task.meta['processed'] += 1

                    task.meta['percent'] = round((task.meta['processed']/task.meta['total']) * 100, 2)
                    task.save()

                message('%s done' % pill.medicine_name)
            except Exception as e:
                print('Exception occured: %s' % e)

            #signals to queue job is done
            self.queue.task_done()


def rxnorm(ndc):
    # ndc value coming from master.py
    # ndc = [array of ndc values]
    if ndc[0] is None:
        return {"rxcui": "", "rxtty": "", "rxstring": ""}
    else:
        # if internet or request throws an error, print out to check connection and exit
        baseurl = 'https://rxnav.nlm.nih.gov/REST/'

        # Searching RXNorm API, Search by identifier to find RxNorm concepts
        # http://rxnav.nlm.nih.gov/REST/rxcui?idtype=NDC&id=0591-2234-10
        # Set url parameters for searching RXNorm for SETID
        ndcSearch = 'rxcui?idtype=NDC&id='

        # Search RXNorm API, Return all properties for a concept
        rxPropSearch = 'rxcui/'
        rxttySearch = '/property?propName=TTY'
        rxstringSearch = '/property?propName=RxNorm%20Name'

        # Request RXNorm API to return json
        header = {'Accept': 'application/json'}

        # Search RXNorm using NDC code, return RXCUI id
        getRXCUI = requests.get(baseurl+ndcSearch+ndc, headers=header, timeout=3)
        rxcuiJSON = getRXCUI.json()
        # Check if first value in list returns a RXCUI, if not go to next value
        try:
            if rxcuiJSON['idGroup']['rxnormId']:
                rxCUI = rxcuiJSON['idGroup']['rxnormId'][0]
                rxProp = requests.get(baseurl + rxPropSearch + rxCUI + '/properties', headers=header, timeout=3)
                rxProperties = rxProp.json()
                rxTTY = rxProperties['properties']['tty']
                rxSTRING = rxProperties['properties']['name']
                return {"rxcui": rxCUI, "rxtty": rxTTY, "rxstring": rxSTRING}
        except KeyError:
            # if last item return null values
            return {"rxcui": "", "rxtty": "", "rxstring": ""}


if __name__ == "__main__":
    # Test with sample NDC codes, one works, one doesn't
    dataTest = rxnorm('66435-101-42')
    print dataTest
