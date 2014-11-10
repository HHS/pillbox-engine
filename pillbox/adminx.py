import xadmin
# from xadmin import views

from pillbox.models import PillBoxData, Characteristic


class PillBoxDataAdmin(object):

    list_display = ('medicine_name', 'setid', 'has_image')
    # list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['splcolor', 'splsize', 'splscore']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True


class CharacteristicAdmin(object):

    list_display = ('type', 'spl_value', 'pillbox_value', 'is_different', 'reason')
    # list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['type', 'is_different']
    search_fields = ['type', 'spl_value', 'pillbox_value']
    reversion_enable = True

xadmin.site.register(PillBoxData, PillBoxDataAdmin)
xadmin.site.register(Characteristic, CharacteristicAdmin)

