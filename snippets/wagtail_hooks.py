from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from snippets.models import Demo, Banner, Book

class BannerAdmin(ModelAdmin):
    model = Banner
    list_display = ('banner_title', 'url')

class BookAdmin(ModelAdmin):
    model = Book
    menu_label = 'Book'
    menu_icon = 'pilcrow'
    list_display = ('title', 'author')

class BannerGroup(ModelAdminGroup):
    menu_label = "Library"
    menu_icon = 'folder-open-inverse'
    # menu_icon = 'fa-cutlery'
    menu_order = 300 # will put in 4th place (000 being 1st, 100 2nd)
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
modeladmin_register(SnippetMenu)
modeladmin_register(BookAdmin)