from enum import Enum

from django.db import models
from django import forms

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


class Type(Enum):
    MOBILE = '移动无线端版本'
    PC = '电脑端版本'


TYPE_DICT = [(Type.MOBILE.name, Type.MOBILE.value),
             (Type.PC.name, Type.PC.value)]


@register_snippet
class Metadata(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="元数据标题",
                             help_text='请输入元素数据标题')
    type = models.CharField(max_length=20,
                            choices=TYPE_DICT,
                            help_text='请选择元数据适用平台')
    url = models.URLField(help_text='请输入元数据跳转链接')
    image = models.ForeignKey('wagtailimages.Image',
                              on_delete=models.CASCADE,
                              related_name='+',
                              help_text='请选择元数据对应的图片资源')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "元数据资源"

    panels = [
        FieldPanel('title'),
        FieldPanel('type', widget=forms.Select),
        ImageChooserPanel('image'),
        FieldPanel('url')
    ]


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
