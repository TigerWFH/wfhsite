from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase
# from wagtail.admin import edit_handlers
# from wagtail.admin.templatetags.wagtailadmin_tags import sidebar_collapsed

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    advert = models.ForeignKey('snippets.Advert',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        SnippetChooserPanel('advert'),
        InlinePanel('advert_placements', label="Adverts")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages

        return context


# snippets集合
class BlogPageSnippetAdverts(Orderable, models.Model):
    page = ParentalKey(BlogIndexPage,
                       on_delete=models.CASCADE,
                       related_name='advert_placements')
    advert = models.ForeignKey('snippets.Advert',
                               on_delete=models.CASCADE,
                               related_name='+')

    class Meta(Orderable.Meta):
        verbose_name = "advert placement"
        verbose_name_plural = "advert placements"

    pannels = [SnippetChooserPanel('advert')]

    def __str__(self):
        return self.page.title + "->" + self.advert.text


class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage',
                                 related_name='tagged_item',
                                 on_delete=models.CASCADE)


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images")
    ]


# 图片集合
# ForeignKey(Django)提供一对多
# OneToOneField(Django)提供一对一
# ManyToManyField(Django)提供多对多
#########################################
# ParentalKey(wagtail)是建立起一对多的关系，且对应的column_name就是related_name
# 1对多，可以通过配置是否是多方进行控制
#########################################
# By defining a ParentalKey with related_name='related_links',
# you set up a one-to-many relation called related_links on BookPage.
# This allows you to retrieve all of the BookPageRelatedLinks objects associated with a given BookPage instance (for example,
# if your BookPage instance was called page, you could write page.related_links.all()).
# The InlinePanel declaration then tells Wagtail to make the related_links property editable within the admin.
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage,
                       on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image',
                              on_delete=models.CASCADE,
                              related_name='+')
    caption = models.CharField(blank=True, max_length=250)

    panels = [ImageChooserPanel('image'), FieldPanel('caption')]
