from django.conf.urls import patterns, url
from pages.views import PageViewSet

page_list = PageViewSet.as_view( {
	"get" : "list"
} )

page_detail = PageViewSet.as_view( {
	"get" : "retrieve"
} )

urlpatterns = patterns( "pages.views",
	url( r"^$", page_list ),
	url( r"^(?P<pk>\d+)$", page_detail ),
)
