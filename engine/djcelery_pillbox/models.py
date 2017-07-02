from django.db import models
from django.utils.translation import ugettext_lazy as _
from celery import states

from djcelery import managers
from djcelery.compat import python_2_unicode_compatible
from djcelery.picklefield import PickledObjectField
from djcelery.models import TASK_STATE_CHOICES


@python_2_unicode_compatible
class TaskMeta(models.Model):
    """Task result/status."""
    task_id = models.CharField(_('task id'), max_length=255, unique=True)
    status = models.CharField(
        _('state'),
        max_length=50, default=states.PENDING, choices=TASK_STATE_CHOICES,
    )
    result = PickledObjectField(null=True, default=None, editable=False)
    date_done = models.DateTimeField(_('done at'), auto_now=True)
    traceback = models.TextField(_('traceback'), blank=True, null=True)
    hidden = models.BooleanField(editable=False, default=False, db_index=True)
    # TODO compression was enabled by mistake, we need to disable it
    # but this is a backwards incompatible change that needs planning.
    meta = PickledObjectField(
        compress=True, null=True, default=None, editable=False,
    )

    objects = managers.TaskManager()

    class Meta:
        verbose_name = _('task state')
        verbose_name_plural = _('task states')
        db_table = 'celery_taskmeta'

    def to_dict(self):
        return {'task_id': self.task_id,
                'status': self.status,
                'result': self.result,
                'date_done': self.date_done,
                'traceback': self.traceback,
                'children': (self.meta or {}).get('children')}

    def __str__(self):
        return '<Task: {0.task_id} state={0.status}>'.format(self)


@python_2_unicode_compatible
class TaskSetMeta(models.Model):
    """TaskSet result"""
    taskset_id = models.CharField(_('group id'), max_length=255, unique=True)
    result = PickledObjectField()
    date_done = models.DateTimeField(_('created at'), auto_now=True)
    hidden = models.BooleanField(editable=False, default=False, db_index=True)

    objects = managers.TaskSetManager()

    class Meta:
        """Model meta-data."""
        verbose_name = _('saved group result')
        verbose_name_plural = _('saved group results')
        db_table = 'celery_tasksetmeta'

    def to_dict(self):
        return {'taskset_id': self.taskset_id,
                'result': self.result,
                'date_done': self.date_done}

    def __str__(self):
        return '<TaskSet: {0.taskset_id}>'.format(self)
