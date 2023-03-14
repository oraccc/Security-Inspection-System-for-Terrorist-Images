from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

class ArticleIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		articlepages = self.get_children().live()
		context['articlepages'] = articlepages
		return context

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]

class ArticlePage(Page):
	date = models.DateField("Post date")
	author = models.CharField(max_length=250,default='Admin')
	intro = models.CharField(max_length=250)
	body = RichTextField(blank=True)

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
		FieldPanel('date'),
		FieldPanel('intro'),
		FieldPanel('body'),
		FieldPanel('author'),
		InlinePanel('gallery_images', label="Gallery images"),
	]

class ArticlePageGalleryImage(Orderable):
	page = ParentalKey(ArticlePage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)
	caption = models.CharField(blank=True, max_length=250)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]