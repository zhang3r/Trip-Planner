from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

	
urlpatterns = [
	# url(r'^$', views.city_list, name='index'),
	# url(r'^$', views.CityList.as_view(), name='index'),
	url(r'^$', views.api_root),
	url(r'^cities/$', views.CityList.as_view()),

	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]