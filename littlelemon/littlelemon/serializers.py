# Serializers define the API representation.
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']