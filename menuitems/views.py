from menuitems.models import MenuItem
from rest_framework import viewsets
from menuitems.serializers import MenuItemSerializer

class MenuItemViewSet( viewsets.ReadOnlyModelViewSet ):
	"""
	Implements REST view for getting index and a single menu item.
	"""
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer

