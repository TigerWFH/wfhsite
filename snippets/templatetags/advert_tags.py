from django import template
from snippets.models import Advert

register = template.Library()


# snippets目录下的templates无效，只能将模板放在配置应用下
# Template-loader
@register.inclusion_tag('snippets/adverts.html', takes_context=True)
def adverts(context):
    return {'adverts': Advert.objects.all(), 'request': context['request']}
