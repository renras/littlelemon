from django.shortcuts import render
from rest_framework import viewsets
from restaurant.models import Booking, MenuItem
from restaurant.serializers import BookingSerializer, MenuItemSerializer

# Create your views here.
def index(request):
  return render(request, 'index.html', {})


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer