from django.db import models

from spl.models import Pill
from pillbox.models import PillBoxData


# Abstract Model
class CommonInfo(models.Model):
    spl_value = models.CharField('SPL Value', max_length=200, null=True, blank=True)
    pillbox_value = models.CharField('Pillbox Value', max_length=200, null=True, blank=True)
    pillbox = models.ForeignKey(PillBoxData)
    spl = models.ForeignKey(Pill)
    verified = models.BooleanField('Verified?', default=False)
    is_different = models.BooleanField('Is Different?', default=False)
    reason = models.TextField('Reason', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Color(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value

    def save(self, *args, **kwargs):
        if getattr(self, 'verified', True):
            pill = PillBoxData.objects.get(pk=self.pillbox_id)
            pill.splcolor = self.pillbox_value
            pill.save()
        super(Color, self).save(*args, **kwargs)


class Score(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value

    def save(self, *args, **kwargs):
        if getattr(self, 'verified', True):
            pill = PillBoxData.objects.get(pk=self.pillbox_id)
            pill.splscore = self.pillbox_value
            pill.save()
        super(Score, self).save(*args, **kwargs)


class Size(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value

    def save(self, *args, **kwargs):
        if getattr(self, 'verified', True):
            pill = PillBoxData.objects.get(pk=self.pillbox_id)
            pill.splsize = self.pillbox_value
            pill.save()
        super(Size, self).save(*args, **kwargs)


class Shape(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value

    def save(self, *args, **kwargs):
        if getattr(self, 'verified', True):
            pill = PillBoxData.objects.get(pk=self.pillbox_id)
            pill.splshape = self.pillbox_value
            pill.save()
        super(Shape, self).save(*args, **kwargs)


class Imprint(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value

    def save(self, *args, **kwargs):
        if getattr(self, 'verified', True):
            pill = PillBoxData.objects.get(pk=self.pillbox_id)
            pill.splimprint = self.pillbox_value
            pill.save()
        super(Imprint, self).save(*args, **kwargs)


class Image(CommonInfo):

    def __unicode__(self):
        return self.pillbox_value

    def save(self, *args, **kwargs):
        if getattr(self, 'verified', True):
            pill = PillBoxData.objects.get(pk=self.pillbox_id)
            pill.splimage = self.pillbox_value
            pill.save()
        super(Image, self).save(*args, **kwargs)
