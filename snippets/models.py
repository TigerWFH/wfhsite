from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover_photo = models.ForeignKey('wagtailimages.Image',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    related_name='+')

    # ImageChooserPanel、PageChooserPanel、DocumentChooserPanel
    panels = [
        FieldPanel('title'),
        FieldPanel('author'),
        ImageChooserPanel('cover_photo')
    ]


class Banner(models.Model):
    banner_title = models.CharField(max_length=255, verbose_name="标题")
    url = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "轮播图"


@register_snippet
class Advert(models.Model):
    # 定义表单域
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)
    # 定义可在管理后台编辑的表单域
    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text

    class Meta:
        # snippet的名字，所有的snippet都是统一放在Snippets菜单下，该菜单名不可以修改
        verbose_name_plural = 'Advert'


@register_snippet
class Demo(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)

    panels = [FieldPanel('name'), FieldPanel('age')]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Demo'
