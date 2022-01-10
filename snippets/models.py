from enum import Enum
from django.core.checks.registry import register

from django.db import models
from django import forms

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
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



# 业务需求组件
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
                              help_text='请选择元数据对应的图片资源',
                              verbose_name='本地图片资源',
                              blank=True)
    img_url = models.URLField(help_text='请输入图片url地址',
                              verbose_name='远程图片资源URL',
                              blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "元数据资源"

    panels = [
        FieldPanel('title'),
        FieldPanel('type', widget=forms.Select),
        FieldPanel('img_url'),
        ImageChooserPanel('image'),
        FieldPanel('url')
    ]


@register_snippet
class Banner(models.Model):
    title = models.CharField(max_length=30,
                             verbose_name='Banner标题',
                             help_text='请输入Banner标题')
    type = models.CharField(max_length=20,
                            choices=TYPE_DICT,
                            help_text='请选择元数据适用平台',
                            default=Type.PC.name)
    first = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第一张轮播图元素数据',
                              null=True,
                              blank=False)
    second = models.ForeignKey('Metadata',
                               on_delete=models.SET_NULL,
                               related_name='+',
                               help_text='请选择第二张轮播图元素数据',
                               null=True,
                               blank=True)
    third = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第三张轮播图元素数据',
                              null=True,
                              blank=True)
    fouth = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第四张轮播图元素数据',
                              null=True,
                              blank=True)
    fifth = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第五张轮播图元素数据',
                              null=True,
                              blank=True)
    sixth = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第六张轮播图元素数据',
                              null=True,
                              blank=True)

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('title'),
        FieldPanel('type', widget=forms.Select),
        SnippetChooserPanel('first'),
        SnippetChooserPanel('second'),
        SnippetChooserPanel('third'),
        SnippetChooserPanel('fouth'),
        SnippetChooserPanel('fifth'),
        SnippetChooserPanel('sixth')
    ]


@register_snippet
class Footer(models.Model):
    # 版权声明copyright
    # 备案声明
    pass

###############################
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
