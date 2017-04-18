from __future__ import division

import sys
import threading
import requests
import simplejson as json

from spl.models import Pill, Task


class ThreadXNorm(threading.Thread):
    def __init__(self, queue, task_id):
        threading.Thread.__init__(self)
        self.queue = queue
        self.task_id = task_id

    def run(self):
        while True:
            #grabs file from queue
            pill_id = self.queue.get()

            pill = Pill.objects.get(pk=pill_id)

            rx = rxnorm(pill.product_code)

            pill.rxstring = rx['rxstring']
            pill.rxtty = rx['rxtty']
            pill.rxcui = rx['rxcui']
            pill.save()

            task = Task.objects.get(pk=self.task_id)

            task.meta['processed'] += 1

            task.meta['percent'] = round((task.meta['processed']/task.meta['total']) * 100, 2)
            task.save()

            print "%s done" % pill.medicine_name

            #signals to queue job is done
            self.queue.task_done()


def rxnorm(ndc):
    # ndc value coming from master.py
    # ndc = [array of ndc values]
    if ndc[0] is None:
        return {"rxcui": "", "rxtty": "", "rxstring": ""}
    else:
        # if internet or request throws an error, print out to check connection and exit
        try:
            baseurl = 'http://rxnav.nlm.nih.gov/REST/'

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

            def getTTY(rxCUI):
                # Search RXNorm again using RXCUI to return RXTTY & RXSTRING
                getTTY = requests.get(baseurl+rxPropSearch+rxCUI+rxttySearch, headers=header)

                ttyJSON = json.loads(getTTY.text, encoding="utf-8")

                return ttyJSON['propConceptGroup']['propConcept'][0]['propValue']

            def getSTRING(rxCUI):
                # Search RXNorm again using RXCUI to return RXTTY & RXSTRING
                getString = requests.get(baseurl+rxPropSearch+rxCUI+rxstringSearch, headers=header)
                stringJSON = json.loads(getString.text, encoding="utf-8")

                return stringJSON['propConceptGroup']['propConcept'][0]['propValue']

            # Search RXNorm using NDC code, return RXCUI id
            getRXCUI = requests.get(baseurl+ndcSearch+ndc, headers=header)
            if getRXCUI.status_code != requests.codes.ok:
                print "RXNorm server response error. Response code: %s" % getRXCUI.status_code
            rxcuiJSON = json.loads(getRXCUI.text, encoding="utf-8")
            # Check if first value in list returns a RXCUI, if not go to next value
            try:
                if rxcuiJSON['idGroup']['rxnormId']:
                    rxCUI = rxcuiJSON['idGroup']['rxnormId'][0]
                    rxTTY = getTTY(rxCUI)
                    rxSTRING = getSTRING(rxCUI)
                    return {"rxcui": rxCUI, "rxtty": rxTTY, "rxstring": rxSTRING}
            except KeyError:
                # if last item return null values
                return {"rxcui": "", "rxtty": "", "rxstring": ""}
        except:
            sys.exit("RXNorm connection")


if __name__ == "__main__":
    # Test with sample NDC codes, one works, one doesn't
    dataTest = rxnorm('66435-101-42')
    print dataTest
