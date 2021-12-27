from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from snippets.models import Demo, Banner

class OtherBannerAdmin(ModelAdmin):
    model = Banner
    list_display = ('banner_title', 'url')

class HomeBannerAdmin(ModelAdmin):
    model = Banner
    list_display = ('banner_title', 'url')

class BannerMenu(ModelAdminGroup):
    menu_label = "轮播配置"
    menu_icon = 'fa-cutlery'
    menu_order = 300 # will put in 4th place (000 being 1st, 100 2nd)
    items = (HomeBannerAdmin, OtherBannerAdmin)

class SnippetMenu(ModelAdmin):
    model = Demo
    list_display = ('name', 'age')
    search_fields = ('name')
    list_filter = ('name')

# 注册
modeladmin_register(BannerMenu)
modeladmin_register(SnippetMenu)