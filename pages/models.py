from django.db import models
from filebrowser.fields import FileBrowseField

class Page( models.Model ):
	"""
	Implements a simple static page.
	"""
	title = models.CharField( max_length = 255 )
	slug = models.SlugField( max_length = 255 )
	thumbnail = FileBrowseField(
		"Image",
		max_length = 255,
		blank = True,
		null = True,
		extensions = [ ".jpg", ".gif", ".png", ".jpeg" ]
	)
	body = models.TextField()

	def __unicode__( self ):
		return self.title

	class Meta:
		ordering = [ "title" ]
