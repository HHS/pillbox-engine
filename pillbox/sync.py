from pillbox.models import PillBoxData, Characteristic
from spl.models import ProductData


def sync():

    pillbox = PillBoxData.objects.all()
    # spl = ProductData.objects.all()
    # print spl
    for pill in pillbox:
        try:
            result = ProductData.objects.get(pk=pill.setid)
            print result
        except ProductData.DoesNotExist:
            print 'didnt exist'



if __name__ == '__main__':

    sync()
