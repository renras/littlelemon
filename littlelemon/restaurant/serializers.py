# Serializers define the API representation.
from rest_framework import serializers
from restaurant.models import Booking, Menu


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'num_guests', 'booking_date']


class MenuSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Menu
    fields = ['id', 'title', 'price', 'inventory']

