from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    banner = models.ForeignKey('snippets.Banner',
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name='+',
                               verbose_name='请选择轮播图')
    nav = models.ForeignKey('snippets.Nav',
                              null=True,
                              on_delete=models.SET_NULL,
                              verbose_name='请选择导航',
                              related_name='+')

    def get_context(self, request):
        # Update template context
        context = super().get_context(request)
        # 对banner数据进行过滤
        banner = self.banner
        if banner:
            bannerList = []
            if banner.first:
                bannerList.append(banner.first)
            if banner.second:
                bannerList.append(banner.second)
            if banner.third:
                bannerList.append(banner.third)
            if banner.fourth:
                bannerList.append(banner.fourth)
            if banner.fifth:
                bannerList.append(banner.fifth)
            if banner.sixth:
                bannerList.append(banner.sixth)
            context['bannerList'] = bannerList
        nav = self.nav
        print('========>' + nav.first.first.title)

        return context

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        SnippetChooserPanel('banner'),
        SnippetChooserPanel('nav')
    ]
