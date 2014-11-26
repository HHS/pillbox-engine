from django.db import models

from spl.models import ProductData
from pillbox.models import PillBoxData


# Abstract Model
class CommonInfo(models.Model):
    spl_value = models.CharField('SPL Value', max_length=200)
    pillbox_value = models.CharField('Pillbox Value', max_length=200)
    pillbox = models.ForeignKey(PillBoxData)
    spl = models.ForeignKey(ProductData)
    is_different = models.BooleanField('Is Different?', default=False)
    reason = models.TextField('Reason', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Color(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value


class Score(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value


class Size(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value


class Shape(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value


class Imprint(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value


class Image(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value
