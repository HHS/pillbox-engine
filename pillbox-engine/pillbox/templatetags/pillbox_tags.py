from django import template
from django.contrib.humanize.templatetags.humanize import naturaltime

from pillbox.models import PillBoxData
from spl.models import Task

register = template.Library()


@register.inclusion_tag('pillbox-engine/tags/widgets.html')
def pillbox_widgets():
    pillbox_count = PillBoxData.objects.all().count()

    boxes = [
        {
            'icon': 'fa-briefcase',
            'name': 'Pillbox Data',
            'count': pillbox_count,
            'text': 'Check Import Status',
            'link': '#',
            'color': 'primary',
            'action': '/pillbox/status/'
        },
        {
            'icon': 'fa-arrows-h ',
            'name': 'Add New',
            'subtitle': 'New SPL pills to Pillbox',
            # 'count': pillbox_count,
            'text': 'New pills from SPL',
            'link': '#',
            'color': 'green',
            'action': '/pillbox/transfer/transfer'
        },
        {
            'icon': 'fa-arrows-h ',
            'name': 'Update',
            'subtitle': 'Compare SPL With Pillbox',
            # 'count': pillbox_count,
            'text': 'Compare',
            'link': '#',
            'color': 'yellow',
            'action': '/pillbox/transfer/compare'
        }
    ]

    options = {
        'transfer': 1,
        'compare': 2
    }

    for k, v in options.iteritems():
        try:
            task = Task.objects.filter(is_active=True, name=k)[:1].get()
            boxes[v]['meta'] = task.meta
            boxes[v]['status'] = task.status

        except Task.DoesNotExist:
            pass

    return {'boxes': boxes}


@register.simple_tag
def pillbox_sync_time():
    last = PillBoxData.objects.all().order_by('-updated_at')[:1]

    try:
        return naturaltime(last[0].updated_at)
    except:
        return 'N/A'
