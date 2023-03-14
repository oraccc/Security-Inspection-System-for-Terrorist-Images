from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
	home_title = RichTextField(blank = True)
	body = RichTextField(blank = True)
    
	content_panels = Page.content_panels + [
		FieldPanel('home_title', classname="full"),
		FieldPanel('body', classname="full"),
	]