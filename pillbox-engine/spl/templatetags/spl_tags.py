from django import template
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.conf import settings

from spl.models import Product, Pill, Ingredient, Source, Task

register = template.Library()


@register.inclusion_tag('pillbox-engine/tags/widgets.html')
def spl_widgets():
    products_count = Product.objects.all().count()
    pills_count = Pill.objects.all().count()
    rxnorm_count = Pill.objects.filter(rxcui__isnull=True).count()

    boxes = [
        {
            'icon': 'fa-stethoscope',
            'name': 'SPL Products',
            'count': products_count,
            'text': 'Sync Data',
            'link': '#',
            'color': 'primary',
            'action': '/spl/sync/products/',
            'action_name': 'products'
        },
        {
            'icon': 'fa-medkit',
            'name': 'OSDF Pills',
            'count': pills_count,
            'text': 'Sync Data',
            'link': '#',
            'color': 'green',
            'action': '/spl/sync/pills/',
            'action_name': 'pills'
        },
        {
            'icon': 'fa-dot-circle-o',
            'name': 'Missing RXNorm',
            'count': rxnorm_count,
            'text': 'View Details',
            'link': '#',
            'color': 'yellow',
            'action_name': None,
            'action': '/spl/sync/rxnorm/',
            'action_name': 'rxnorm'
        }]

    try:
        task = Task.objects.filter(is_active=True, download_type__isnull=True)[:1].get()
        for box in boxes:
            if task.name == box['action_name']:
                box['meta'] = task.meta
                box['status'] = task.status

    except Task.DoesNotExist:
        pass

    return {'boxes': boxes}


@register.inclusion_tag('pillbox-engine/tags/widgets.html')
def download_widgets():

    sources = Source.objects.all().order_by('title')

    colors = iter(['primary', 'green', 'yellow', 'red',
                   'primary', 'green', 'yellow', 'red'])
    boxes = []
    for source in sources:

        box = {
            'icon': 'fa-download',
            'name': source.title,
            'text': 'Download New Data',
            'link': '#',
            'color': colors.next(),
            'action': '/spl/download/%s/' % source.id,
            'time': source.last_downloaded
        }
        try:
            task = Task.objects.filter(is_active=True, download_type=source.title)[:1].get()
            box['meta'] = task.meta
            box['status'] = task.status
        except Task.DoesNotExist:
            pass

        boxes.append(box)

    return {'boxes': boxes}


@register.inclusion_tag('pillbox-engine/tags/size_widgets.html')
def size_widgets():

    sources = Source.objects.all()

    sunzip = 0
    szip = 0

    for s in sources:
        if s.unzip_size:
            sunzip += s.unzip_size
        if s.zip_size:
            szip += s.zip_size

    boxes = [
        {
            'size': round(szip / 1000000000, 2),
            'path': settings.DOWNLOAD_PATH,
            'name': 'Zip Folder Size',
            'color': 'yellow'
        },
        {
            'size': round(sunzip / 1000000000, 2),
            'path': settings.SOURCE_PATH,
            'name': 'Unzip Folder Size',
            'color': 'red'
        }
    ]

    return {'boxes': boxes}


@register.simple_tag
def spl_sync_time():
    try:
        last = Pill.objects.all().order_by('-updated_at')[0:1].get()
        return naturaltime(last.updated_at)
    except Pill.DoesNotExist:
        return 'N/A'
