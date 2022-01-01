from django import template
from snippets.models import Demo

register = template.Library()


@register.inclusion_tag('snippets/demo.html', takes_context=True)
def demos(context):
    return {'demos': Demo.objects.all(), 'request': context['request']}
