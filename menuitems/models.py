from django.db import models

class MenuItem( models.Model ):
	title = models.CharField( max_length = 255 )
	url = models.CharField( max_length = 255 )
	parent = models.ForeignKey( "self", blank = True, null = True, related_name = "children" )

	def __unicode__( self ):
		return self.title
