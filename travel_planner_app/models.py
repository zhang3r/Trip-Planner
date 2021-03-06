from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.

class Trip(models.Model):
	trip_name = models.CharField(max_length=200)



class City(models.Model):
	# trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
	owner = models.ForeignKey('auth.User', related_name='cities')
	city_name = models.CharField(max_length=200)
	city_date = models.DateField(default=date.today)
	city_latitude =  models.DecimalField(decimal_places=3, max_digits=10)
	city_longitude = models.DecimalField(decimal_places=3, max_digits=10)

	def save(self, *args, **kwargs):
		super(City, self).save(*args,**kwargs)

	class Meta:
		ordering = ('city_date','owner')


class Flight(models.Model):
	flight_origin_city =  models.ForeignKey(City, on_delete=models.CASCADE)
	# flight_dest_city = models.CharField(max_length=200)
	flight_num = models.CharField(max_length=200)
	flight_carrier = models.CharField(max_length=200)
	flight_cost = models.DecimalField(decimal_places=2, max_digits=10)

class Hotel(models.Model):
	hotel_name = models.CharField(max_length=200)
	hotel_address = models.CharField(max_length=200)
	hotel_cost = models.DecimalField(decimal_places=2, max_digits=10)