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

# Create your models here.
class IMG(models.Model):
    img = models.ImageField(upload_to='upload')

class IMG_Person(models.Model):
	img = models.ImageField(upload_to='upload_person')

class UploadIndexPage(Page):
	intro = RichTextField(blank=True)
	context_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]
