from rest_framework import serializers
from travel_planner_app.models import City
from travel_planner_app.models import Trip
from datetime import date


class CitySerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	city_name = serializers.CharField(required=True, max_length=200)
	city_date = serializers.DateField( default=date.today)
	city_latitude =  serializers.DecimalField(decimal_places=3, max_digits=10)
	city_longitude = serializers.DecimalField(decimal_places=3, max_digits=10)

	def create(self, validated_data):
		"""
		Create and return a new 'City' given validated_data
		"""
		return City.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing 'City' instance, given the validated data.
		"""
		# instance.trip = validated_data.get('trip', instance.trip)
		instance.city_name = validated_data.get('city_name', instance.city_name)
		instance.city_date = validated_data.get('city_date', instance.city_date)
		instance.city_latitude = validated_data.get('city_latitude', instance.city_latitude)
		instance.city_longitude = validated_data.get('city_longitude', instance.city_longitude)

		instance.save()
		return instance


class TripSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trip
		fields= ('id','trip_name')