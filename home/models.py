from django.db import models
from django.db.models.functions.text import Ord
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    def banner_list(self):
        banner_list = self.banner.first()
        print(banner_list)
        if banner_list:
            return banner_list
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('banner', label='请选择banner资源')
    ]

class HomeBanner(Orderable):
    page = ParentalKey(
        HomePage,
        on_delete=models.SET_NULL,
        related_name='banner',
        null=True
        )
    title = models.CharField(max_length=20, blank=False)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
        )
    type = models.CharField(max_length=10, blank=False)
    url = models.URLField()

    panels = [
        FieldPanel('title'),
        FieldPanel('type'),
        ImageChooserPanel('image'),
        FieldPanel('url')
    ]

