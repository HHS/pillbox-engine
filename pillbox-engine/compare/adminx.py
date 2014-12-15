import xadmin
# from xadmin import views

from compare.models import Color, Score, Size, Shape, Image, Imprint


class GenericAdmin(object):
    def pillbox_image(self, instance):
        if instance.pillbox.splimage:
            return '<img height="90" src="%s" />' % instance.pillbox.splimage.url
        else:
            return ''
    pillbox_image.short_description = "Pillbox"
    pillbox_image.allow_tags = True
    pillbox_image.is_column = True

    def spl_image(self, instance):
        if instance.spl.splimage:
            return '<img height="90" src="%s" />' % instance.spl.splimage.url
        else:
            return ''
    spl_image.short_description = "SPL"
    spl_image.allow_tags = True
    spl_image.is_column = True

    list_editable = ('pillbox_value', 'verified', 'is_different')

    list_display = ('spl_value', 'pillbox_value', 'verified', 'is_different', 'pillbox_image', 'spl_image', 'pillbox')

    readonly_fields = ['spl', 'pillbox', 'spl_value']

    fields = ['spl', 'pillbox', 'spl_value', 'pillbox_value', 'verified',
              'is_different', 'reason']

    list_filter = ['verified', 'pillbox__new', 'pillbox__updated']

    list_per_page = 10

    ordering = ['verified']


class ColorAdmin(GenericAdmin):

    model_icon = 'fa fa-adjust'


class ScoreAdmin(GenericAdmin):

    model_icon = 'fa fa-trophy'


class SizeAdmin(GenericAdmin):

    model_icon = 'fa fa-magic'


class ShapeAdmin(GenericAdmin):

    model_icon = 'fa fa-stop'


class ImageAdmin(GenericAdmin):

    model_icon = 'fa fa-camera-retro'


class ImprintAdmin(GenericAdmin):

    model_icon = 'fa fa-asterisk'


xadmin.site.register(Color, ColorAdmin)
xadmin.site.register(Score, ScoreAdmin)
xadmin.site.register(Size, SizeAdmin)
xadmin.site.register(Shape, ShapeAdmin)
xadmin.site.register(Image, ImageAdmin)
xadmin.site.register(Imprint, ImprintAdmin)

