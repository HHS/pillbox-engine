import xadmin
# from xadmin import views

from pillbox.models import PillBoxData


class PillBoxDataAdmin(object):

    list_display = ('medicine_name', 'setid', 'has_image')
    # list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['splcolor', 'splsize', 'splscore']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True

xadmin.site.register(PillBoxData, PillBoxDataAdmin)
