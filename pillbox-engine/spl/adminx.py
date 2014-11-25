import xadmin
from xadmin import views

from spl.models import Source, Ingredient, SetInfo, ProductData


class GlobalSetting(object):
    global_search_models = [Source]
    # global_models_icon = {
    #     Source: 'fa fa-laptop', Ingredient: 'fa fa-cloud'
    # }
    menu_style = 'default'  # 'accordion'
    site_title = 'Pillbox Engine'
    site_footer = 'Pillbox'
xadmin.site.register(views.CommAdminView, GlobalSetting)


class SourceAdmin(object):

    search_fields = ['title']
    reversion_enable = True


class IngredientAdmin(object):

    list_display = ('name', 'code_system', 'class_code')
    list_filter = ['code_system', 'class_code']
    list_quick_filter = ['class_code']
    search_fields = ['name']
    reversion_enable = True


class SetInfoAdmin(object):

    list_display = ('setid', 'title', 'source', 'version_number', 'author', 'is_osdf',
                    'effective_time', 'version_number')
    list_filter = ['version_number', 'is_osdf']
    list_quick_filter = ['is_osdf', 'source']
    search_fields = ['title', 'setid', 'author', 'author_legal', 'filename']
    reversion_enable = True


class ProductDataAdmin(object):

    list_display = ('medicine_name', 'setid', 'product_code', 'part_num', 'dosage_form')
    list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['splcolor', 'splsize', 'splscore']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True


xadmin.site.register(Source, SourceAdmin)
xadmin.site.register(Ingredient, IngredientAdmin)
xadmin.site.register(SetInfo, SetInfoAdmin)
xadmin.site.register(ProductData, ProductDataAdmin)
