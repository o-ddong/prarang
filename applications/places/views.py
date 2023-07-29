from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from applications.places.models import Restaurant, Pray
from applications.places.serializer import PraySerializer, RestaurantSerializer


# Create your views here.


class PlaceViewSet(mixins.ListModelMixin, GenericViewSet):

    @action(methods=["GET"], detail=False, url_path="prayer-room")
    def pray(self, request):
        queryset = Pray.objects.all().order_by('-id')
        serializer = PraySerializer(queryset, many=True)
        data_response = {
            "message": "OPERATION_SUCCESS",
            "results": serializer.data
        }
        return Response(data_response)

    @action(methods=["GET"], detail=False, url_path="restaurant")
    def restaurant(self, request):
        queryset = Restaurant.objects.all().order_by('-id')
        serializer = RestaurantSerializer(queryset, many=True)
        data_response = {
            "message": "OPERATION_SUCCESS",
            "results": serializer.data
        }
        return Response(data_response)

