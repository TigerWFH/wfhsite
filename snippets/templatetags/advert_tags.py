from django import template
from snippets.models import Advert

register = template.Library()


# Template-loader
@register.inclusion_tag('snippets/adverts.html', takes_context=True)
def adverts(context):
    return {'adverts': Advert.objects.all(), 'request': context['request']}
