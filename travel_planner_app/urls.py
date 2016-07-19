from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

	
urlpatterns = [
	url(r'^$', views.city_list, name='index'),
	url(r'^cities/$', views.CityList.as_view())
]