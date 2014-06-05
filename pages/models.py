from django.db import models

class Page( models.Model ):
	"""
	Implements a simple static page.
	"""
	title = models.CharField( max_length = 255 )
	slug = models.SlugField( max_length = 255 )
	body = models.TextField()

	class Meta:
		ordering = [ "title" ]
