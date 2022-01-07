from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from snippets.models import Demo, Metadata, Book


class BannerAdmin(ModelAdmin):
    model = Metadata
    list_display = ('title', 'url')


class BookAdmin(ModelAdmin):
    model = Book
    menu_label = 'Book'
    menu_icon = 'pilcrow'
    list_display = ('title', 'author')


class BannerGroup(ModelAdminGroup):
    menu_label = "资源库"
    menu_icon = 'folder-open-inverse'
    # menu_icon = 'fa-cutlery'
    # will put in 4th place (000 being 1st, 100 2nd)
    menu_order = 300
    items = (BannerAdmin, BookAdmin)


class SnippetMenu(ModelAdmin):
    model = Demo
    menu_label = 'self'
    menu_icon = 'pilcrow'
    list_display = ('name', 'age')


class BookAdmin(ModelAdmin):
    model = Book
    menu_label = 'Book'
    menu_icon = 'pilcrow'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explore = False
    list_display = ('title', 'author')
    list_filter = ('author')
    search_fields = ('title', 'author')


# 注册
modeladmin_register(BannerGroup)
# modeladmin_register(SnippetMenu)
# modeladmin_register(BookAdmin)