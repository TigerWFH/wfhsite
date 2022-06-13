from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup,
                                                modeladmin_register)
# from snippets.models import Demo, Metadata, Book
from snippets.models import Demo, Metadata, Banner


class MetadataAdmin(ModelAdmin):
    model = Metadata
    list_display = ('title', 'url')


class BannerAdmin(ModelAdmin):
    model = Banner
    list_display = ('title', 'type')


class SnippetMenu(ModelAdmin):
    model = Demo
    menu_label = 'Demo'
    menu_icon = 'pilcrow'
    list_display = ('name', 'age')


class BannerGroup(ModelAdminGroup):
    menu_label = "资源库"
    menu_icon = 'folder-open-inverse'
    # menu_icon = 'fa-cutlery'
    # will put in 4th place (000 being 1st, 100 2nd)
    menu_order = 300
    items = (MetadataAdmin, BannerAdmin, SnippetMenu)


# 注册
modeladmin_register(BannerGroup)
