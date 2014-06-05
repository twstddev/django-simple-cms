from pages.models import Page
from rest_framework import viewsets
from pages.serializers import PageSerializer

class PageViewSet( viewsets.ReadOnlyModelViewSet ):
	"""
	Implements REST view for getting index and a single page.
	"""
	queryset = Page.objects.all()
	serializer_class = PageSerializer
