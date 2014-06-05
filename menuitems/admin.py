from django.contrib import admin
from menuitems.models import MenuItem
from django_mptt_admin.admin import DjangoMpttAdmin

class MenuItemAdmin( DjangoMpttAdmin ):
	fields = ( "title", "url", )

admin.site.register( MenuItem, MenuItemAdmin )
