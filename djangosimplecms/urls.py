from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
	url( r"^admin/filebrowser/", include( site.urls ) ),
	url( r"^grappelli/", include( "grappelli.urls" ) ),
    url(r'^admin/', include(admin.site.urls)),
	url( r"^api/menuitems/", include( "menuitems.api" ) ),
	url( r"^api/pages/", include( "pages.api" ) ),
)
