from django import template
from django.contrib.humanize.templatetags.humanize import naturaltime

from pillbox.models import PillBoxData

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
        }]

    return {'boxes': boxes}


@register.simple_tag
def pillbox_sync_time():
    last = PillBoxData.objects.all().order_by('-updated_at')[:1]

    try:
        return naturaltime(last[0].updated_at)
    except:
        return 'N/A'
