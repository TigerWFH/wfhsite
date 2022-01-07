from django.db import models
from django.db.models.functions.text import Ord
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

class HomePage(Page):
    body = RichTextField(blank=True)
    metadata = models.ForeignKey(
        'snippets.Metadata',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='请选择元数据'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        SnippetChooserPanel('metadata'),
        InlinePanel('banner', label='请选择banner资源')
    ]

class HomeBanner(Orderable, models.Model):
    page = ParentalKey(
        HomePage,
        on_delete=models.SET_NULL,
        related_name='banner',
        null=True
        )
    metadata = models.ForeignKey(
        'snippets.Metadata',
        on_delete=models.CASCADE,
        null=True,
        related_name='+',
    )

    panels = [
        SnippetChooserPanel('metadata')
    ]

    def __str__(self):
        return self.page.title + '->' + self.metadata.title

