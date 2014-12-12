import xadmin
# from xadmin import views

from compare.models import Color, Score, Size, Shape, Image, Imprint


class GenericAdmin(object):
    def image_column(self, instance):
        return '<img height="90" src="%s" />' % instance.pillbox.splimage.url
    image_column.short_description = "Image"
    image_column.allow_tags = True
    image_column.is_column = True

    list_editable = ('pillbox_value', 'verified')

    list_display = ('spl_value', 'pillbox_value', 'verified', 'image_column')

    readonly_fields = ['spl', 'pillbox', 'spl_value']

    fields = ['spl', 'pillbox', 'spl_value', 'pillbox_value', 'verified',
              'is_different', 'reason']



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

