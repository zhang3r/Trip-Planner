from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import City

def index(request):
	list_city = City.objects.order_by('-city_date')
	context = {
		'list_city' : list_city
	}
	return render(request, 'travel_planner_app/index.html',context)