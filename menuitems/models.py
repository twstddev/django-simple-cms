from django.db import models
from mptt.models import TreeForeignKey, MPTTModel

class MenuItem( MPTTModel ):
	title = models.CharField( max_length = 255 )
	url = models.CharField( max_length = 255 )
	parent = TreeForeignKey( "self", blank = True, null = True, related_name = "children" )

	def __unicode__( self ):
		return self.title
