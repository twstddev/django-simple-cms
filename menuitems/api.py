from django.conf.urls import patterns, url
from menuitems.views import MenuItemViewSet

menu_item_list = MenuItemViewSet.as_view( {
	"get" : "list",
} )

menu_item_detail = MenuItemViewSet.as_view( {
	"get" : "retrieve",
} )

urlpatterns = patterns( "menuitems.views",
	url( r"^$", menu_item_list ),
	url( r"^(?P<pk>\d+)$", menu_item_detail ),
)
