from rest_framework import serializers

from applications.places.models import Pray, Restaurant


class PraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pray
        fields = "__all__"


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
