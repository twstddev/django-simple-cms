from rest_framework import serializers
from menuitems.models import MenuItem

class MenuItemSerializer( serializers.ModelSerializer ):
	"""
	Serializes menu item model for REST representation.
	"""
	class Meta:
		model = MenuItem
		fields = ( 
			"id",
			"title",
			"url",
			"parent",
		)
	
