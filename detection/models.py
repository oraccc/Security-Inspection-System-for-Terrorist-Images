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

# Models for Separate Detection

# Picture Detection Models
class PictureDetectionIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):

		context = super().get_context(request)
		picturedetectionpages = self.get_children().live()
		context['picturedetectionpages'] = picturedetectionpages
		return context

	context_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]

	
class PictureDetectionPage(Page):
	intro = models.CharField(max_length=250)
	body = models.CharField(max_length=250, blank=True)
	classification = models.CharField(max_length=250, blank=True)


	search_fields = Page.search_fields + [
		index.SearchField('intro'),
		index.SearchField('body'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		FieldPanel('body'),
		FieldPanel('classification'),
		InlinePanel('intro_images', label="Intro images"),
	]

class PictureDetectionPageIntroImage(Orderable):
	page = ParentalKey(PictureDetectionPage, on_delete=models.CASCADE, related_name='intro_images')
	intro_image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('intro_image'),
	]


# Pic-Text Detection Models
class DetectionIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):

		context = super().get_context(request)
		detectionpages = self.get_children().live()
		context['detectionpages'] = detectionpages
		return context

	context_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]

	
class DetectionPage(Page):
	intro = models.CharField(max_length=250)
	count = models.CharField(max_length=250, blank=True)
	body = models.CharField(max_length=250, blank=True)
	result = models.CharField(max_length=250, blank=True)


	search_fields = Page.search_fields + [
		index.SearchField('intro'),
		index.SearchField('body'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		FieldPanel('body'),
		FieldPanel('count'),
		FieldPanel('result'),
		InlinePanel('intro_images', label="Intro images"),
		InlinePanel('psenet_images', label="Psenet images"),
		InlinePanel('result_images', label="Result images"),
		InlinePanel('gallery_images', label="Gallery images"),
	]

class DetectionPageGalleryImage(Orderable):
	page = ParentalKey(DetectionPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)
	caption = models.CharField(blank=True, max_length=250)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]


class DetectionPageIntroImage(Orderable):
	page = ParentalKey(DetectionPage, on_delete=models.CASCADE, related_name='intro_images')
	intro_image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('intro_image'),
	]


class DetectionPageResultImage(Orderable):
	page = ParentalKey(DetectionPage, on_delete=models.CASCADE, related_name='result_images')
	result_image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('result_image'),
	]


class DetectionPagePsenetImage(Orderable):
	page = ParentalKey(DetectionPage, on_delete=models.CASCADE, related_name='psenet_images')
	psenet_image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('psenet_image'),
	]

# Person Detection Models


class PersonDetectionIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):

		context = super().get_context(request)
		persondetectionpages = self.get_children().live()
		context['persondetectionpages'] = persondetectionpages
		return context

	context_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]


class PersonDetectionPage(Page):
	intro = models.CharField(max_length=250)
	result = models.CharField(max_length=250, blank=True)
	name = models.CharField(max_length=250, blank=True)


	search_fields = Page.search_fields + [
		index.SearchField('intro'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		FieldPanel('result'),
		FieldPanel('name'),
		InlinePanel('result_images', label="Result images"),
		InlinePanel('head_images', label="Head images"),
		InlinePanel('gallery_images', label="Gallery images"),
	]


class PersonDetectionPageIntroImage(Orderable):
	page = ParentalKey(PersonDetectionPage, on_delete=models.CASCADE, related_name='intro_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]


class PersonDetectionPageResultImage(Orderable):
	page = ParentalKey(PersonDetectionPage, on_delete=models.CASCADE, related_name='result_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]


class PersonDetectionPageHeadImage(Orderable):
	page = ParentalKey(PersonDetectionPage, on_delete=models.CASCADE, related_name='head_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]


class PersonDetectionPageGalleryImage(Orderable):
	page = ParentalKey(PersonDetectionPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]

# Flag Detection Models


class FlagDetectionIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):

		context = super().get_context(request)
		flagdetectionpages = self.get_children().live()
		context['flagdetectionpages'] = flagdetectionpages
		return context

	context_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]


class FlagDetectionPage(Page):
	intro = models.CharField(max_length=250)
	result = models.CharField(max_length=250, blank=True)


	search_fields = Page.search_fields + [
		index.SearchField('intro'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		FieldPanel('result'),
		InlinePanel('result_images', label="Result images"),
	]


class FlagDetectionPageResultImage(Orderable):
	page = ParentalKey(FlagDetectionPage, on_delete=models.CASCADE, related_name='result_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]


# Models for Joint Detection

class JointDetectionIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):

		context = super().get_context(request)
		jointdetectionpages = self.get_children().live()
		context['jointdetectionpages'] = jointdetectionpages
		return context

	context_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]

class JointDetectionPage(Page):
	intro = models.CharField(max_length=250)
	# 暴恐图片检测
	resnet_result = models.CharField(max_length=250, blank=True)
	resnet_rank = models.CharField(max_length=250, blank=True)
	resnet_href = models.CharField(max_length=250, blank=True)
	gun_result = models.CharField(max_length=250, blank=True)
	classification = models.CharField(max_length=250, blank=True)

	# 暴恐图文检测
	psenet_result = models.CharField(max_length=250, blank=True)
	psenet_count = models.CharField(max_length=250, blank=True)
	psenet_body = models.CharField(max_length=250, blank=True)
	psenet_href = models.CharField(max_length=250, blank=True)

	# 暴恐头目检测
	facenet_result = models.CharField(max_length=250, blank=True)
	facenet_body = models.CharField(max_length=250, blank=True)

	# 暴恐旗帜检测
	maskrcnn_result = models.CharField(max_length=250, blank=True)

	


	search_fields = Page.search_fields + [
		index.SearchField('intro'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		FieldPanel('resnet_result'),
		FieldPanel('resnet_rank'),
		FieldPanel('resnet_href'),
		FieldPanel('gun_result'),
		FieldPanel('classification'),
		FieldPanel('psenet_result'),
		FieldPanel('psenet_count'),
		FieldPanel('psenet_body'),
		FieldPanel('psenet_href'),
		FieldPanel('facenet_result'),
		FieldPanel('facenet_body'),
		FieldPanel('maskrcnn_result'),

		InlinePanel('intro_images', label="Intro images"),
		InlinePanel('resnet_images', label="Resnet images"),
		InlinePanel('gun_images', label="Gun images"),
		InlinePanel('psenet_images', label="Psenet images"),
		InlinePanel('joint_images', label="Joint images"),
		InlinePanel('facenet_images', label="Facenet images"),
		InlinePanel('maskrcnn_images', label="Maskrcnn images"),
	]

class JointDetectionPageIntroImage(Orderable):
	page = ParentalKey(JointDetectionPage, on_delete=models.CASCADE, related_name='intro_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]

class JointDetectionPageGunImage(Orderable):
	page = ParentalKey(JointDetectionPage, on_delete=models.CASCADE, related_name='gun_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]

class JointDetectionPageResnetImage(Orderable):
	page = ParentalKey(JointDetectionPage, on_delete=models.CASCADE, related_name='resnet_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]

class JointDetectionPagePsenetImage(Orderable):
	page = ParentalKey(JointDetectionPage, on_delete=models.CASCADE, related_name='psenet_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]

class JointDetectionPageJointImage(Orderable):
	page = ParentalKey(JointDetectionPage, on_delete=models.CASCADE, related_name='joint_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]

class JointDetectionPageFacenetImage(Orderable):
	page = ParentalKey(JointDetectionPage, on_delete=models.CASCADE, related_name='facenet_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]

class JointDetectionPageMaskrcnnImage(Orderable):
	page = ParentalKey(JointDetectionPage, on_delete=models.CASCADE, related_name='maskrcnn_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)

	panels = [
		ImageChooserPanel('image'),
	]
