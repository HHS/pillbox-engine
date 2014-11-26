import xadmin
# from xadmin import views

from compare.models import Color, Score, Size, Shape, Image, Imprint


class GenericAdmin(object):

    list_display = ('spl_value', 'pillbox_value')


class ColorAdmin(GenericAdmin):
    pass


class ScoreAdmin(GenericAdmin):
    pass


class SizeAdmin(GenericAdmin):
    pass


class ShapeAdmin(GenericAdmin):
    pass


class ImageAdmin(GenericAdmin):
    pass


class ImprintAdmin(GenericAdmin):
    pass


xadmin.site.register(Color, ColorAdmin)
xadmin.site.register(Score, ScoreAdmin)
xadmin.site.register(Size, SizeAdmin)
xadmin.site.register(Shape, ShapeAdmin)
xadmin.site.register(Image, ImageAdmin)
xadmin.site.register(Imprint, ImprintAdmin)

