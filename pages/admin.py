from django.contrib import admin
from pages.models import Page

class PageAdmin( admin.ModelAdmin ):
	prepopulated_fields = { "slug" : ( "title", ) }

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/grappelli/tinymce_setup/tinymce_setup.js',
		]

admin.site.register( Page, PageAdmin )
