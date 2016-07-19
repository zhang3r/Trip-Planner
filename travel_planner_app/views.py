from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import City
from .serializers import CitySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

def index(request):
	list_city = City.objects.order_by('-city_date')
	context = {
		'list_city' : list_city
	}
	return render(request, 'travel_planner_app/index.html',context)


# class JSONResponse(HttpResponse):
# 	"""
# 	an HttpResponse that renders its content into JSON
# 	"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
# def city_list(request):
# 	"""
# 	List all city or create a new city
# 	"""

# 	if request.method == 'GET':
# 		cities = City.objects.all()
# 		serializer = CitySerializer(cities, many=True)
# 		return JSONResponse(serializer.data)
# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = CitySerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data, status=201)
# 		return JSONResponse(serializer.errors, status=400)


# @api_view(['GET','POST'])
# def city_list(request):
# 	"""
# 	List all city or create a new city
# 	"""
# 	if request.method =='GET':
# 		cities = City.objects.all()
# 		serializer = CitySerializer(cities, many=True)
# 		return Response(serializer.data)
# 	elif request.method == 'POST':
# 		serializer = CitySerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CityList(APIView):
# 	"""
# 	List all cities or create a new city
# 	"""
# 	def get(self, request, format=None):
# 		cities = City.objects.all()
# 		serializer = CitySerializer(cities, many=True)
# 		return Response(serailizer.data)

# 	def post(self, request, format=None):
# 		serialzier = CitySerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CityList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# 	queryset = City.objects.all()
# 	serializer_class = CitySerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request,*args,**kwargs)

# 	def post(self,request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

class CityList(generics.ListcreateAPIView):
	queryset = City.objects.all()
	serializer_class = CitySerializer