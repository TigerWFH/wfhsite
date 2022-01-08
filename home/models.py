from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    banner = models.ForeignKey('snippets.Banner',
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name='+',
                               verbose_name='请选择Banner')

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        SnippetChooserPanel('banner')
    ]
