from django import template
from django.contrib.humanize.templatetags.humanize import naturaltime

from spl.models import SetInfo, ProductData, Ingredient, Download

register = template.Library()


@register.inclusion_tag('pillbox-engine/tags/widgets.html')
def spl_widgets():
    products_count = SetInfo.objects.all().count()
    pills_count = ProductData.objects.all().count()
    ingredient_count = Ingredient.objects.all().count()

    boxes = [
        {
            'icon': 'fa-stethoscope',
            'name': 'SPL Products',
            'count': products_count,
            'text': 'Sync Data',
            'link': '#',
            'color': 'primary',
            'action': '/spl/sync/products/',
        },
        {
            'icon': 'fa-medkit',
            'name': 'OSDF Pills',
            'count': pills_count,
            'text': 'Sync Data',
            'link': '#',
            'color': 'green',
            'action': '/spl/sync/pills/',
        },
        {
            'icon': 'fa-dot-circle-o',
            'name': 'Ingredients',
            'count': ingredient_count,
            'text': 'View Details',
            'link': '/spl/ingredient/',
            'color': 'yellow',
        }]

    return {'boxes': boxes}


@register.inclusion_tag('pillbox-engine/tags/download_widgets.html')
def download_widgets():
    # download = Download.objects.filter(completed=True).order_by('-ended')[0:1].get()
    download = Download.objects.all()[0:1].get()
    box = {
        'icon': 'fa-download',
        'name': 'Download',
        'time': download.started,
        'text': 'Download New Data',
        'link': '#',
        'color': 'red',
        'action': '/spl/download/',
    }
    return {'box': box}


@register.simple_tag
def spl_sync_time():
    last = ProductData.objects.all().order_by('-updated_at')[0:1].get()
    time_since(last.updated_at)


def time_since(t):
    try:
        return naturaltime(t)
    except:
        return 'N/A'
