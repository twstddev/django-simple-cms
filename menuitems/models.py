from django.db import models

class MenuItem( models.Model ):
	title = models.CharField( max_length = 255 )
	url = models.CharField( max_length = 255 )
