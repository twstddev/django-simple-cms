from rest_framework import serializers
from pages.models import Page

class PageSerializer( serializers.ModelSerializer ):
	"""
	Serializes pages model for REST representation.
	"""
	class Meta:
		model = Page
