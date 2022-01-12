from enum import Enum

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
    ALL = '适用所有平台'
    MOBILE = '移动无线端版本'
    PC = '电脑端版本'


TYPE_DICT = [(Type.MOBILE.name, Type.MOBILE.value),
             (Type.PC.name, Type.PC.value),
             (Type.ALL.name, Type.ALL.value)]


# 元数据
@register_snippet
class Metadata(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="元数据标题",
                             help_text='请输入元素数据标题')
    label = models.CharField(max_length=50, verbose_name='展示标题', help_text = '请输入元数据展示标题', blank=True)
    type = models.CharField(max_length=20,
                            choices=TYPE_DICT,
                            help_text='请选择元数据适用平台')
    url = models.URLField(help_text='请输入元数据跳转链接')
    image = models.ForeignKey('wagtailimages.Image',
                              null=True,
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
        verbose_name_plural = "元数据"

    panels = [
        FieldPanel('title'),
        FieldPanel('label'),
        FieldPanel('type', widget=forms.Select),
        FieldPanel('url'),
        FieldPanel('img_url'),
        ImageChooserPanel('image'),
    ]


# 元数据集合（支持业务：Banner、Menu）
@register_snippet
class Banner(models.Model):
    title = models.CharField(max_length=30,
                             verbose_name='元数据集合标题',
                             help_text='请输入元数据集合标题')
    type = models.CharField(max_length=20,
                            choices=TYPE_DICT,
                            help_text='请选择元数据适用平台',
                            default=Type.PC.name)
    first = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第一个元数据',
                              null=True,
                              blank=False)
    second = models.ForeignKey('Metadata',
                               on_delete=models.SET_NULL,
                               related_name='+',
                               help_text='请选择第二个元数据',
                               null=True,
                               blank=True)
    third = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第三个元数据',
                              null=True,
                              blank=True)
    fourth = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第四个元数据',
                              null=True,
                              blank=True)
    fifth = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第五个元数据',
                              null=True,
                              blank=True)
    sixth = models.ForeignKey('Metadata',
                              on_delete=models.SET_NULL,
                              related_name='+',
                              help_text='请选择第六个元数据',
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
        SnippetChooserPanel('fourth'),
        SnippetChooserPanel('fifth'),
        SnippetChooserPanel('sixth')
    ]

    class Meta:
        verbose_name_plural = '元数据集合'


@register_snippet
class Nav(models.Model):
    title = models.CharField(max_length=30, verbose_name='请输入导航栏名称')
    first = models.ForeignKey('Banner', null=True, default=None, blank=True, on_delete=models.SET_DEFAULT, help_text='请选择第一个导航菜单', related_name='+')
    second = models.ForeignKey('Banner', null=True, default=None, blank=True, on_delete=models.SET_DEFAULT, help_text='请选择第一个导航菜单', related_name='+')
    third = models.ForeignKey('Banner', null=True, default=None, blank=True, on_delete=models.SET_DEFAULT, help_text='请选择第一个导航菜单', related_name='+')
    fourth = models.ForeignKey('Banner', null=True, default=None, blank=True, on_delete=models.SET_DEFAULT, help_text='请选择第一个导航菜单', related_name='+')
    fifth = models.ForeignKey('Banner', null=True, default=None, blank=True, on_delete=models.SET_DEFAULT, help_text='请选择第一个导航菜单', related_name='+')

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('title'),
        SnippetChooserPanel('first'),
        SnippetChooserPanel('second'),
        SnippetChooserPanel('third'),
        SnippetChooserPanel('fourth'),
        SnippetChooserPanel('fifth'),
    ]

    class Meta:
        verbose_name_plural = '导航栏（Nav）'

@register_snippet
class Footer(models.Model):
    # 版权声明copyright
    copyright = models.CharField(max_length=255)
    # 备案声明：ICP license（商业网站），京ICP证123456789；ICP filing（非商业网站），京ICP备1234567
    icp_license = models.CharField(max_length=255)
    # 沪公网安备12313131，公网安备也就是把网站到公安机关备案，是一套独立的备案系统，相当于让公安机关知道您的网站。现在让多省、市都要求网站开通后一个月内强制办理
    police_license = models.CharField(max_length=255)
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
