from django.urls import path, include
from .views import index, BookingViewSet, MenuViewSet
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'menus', MenuViewSet)

urlpatterns = [
  path('', index, name='index'),
  path('', include(router.urls)),
]