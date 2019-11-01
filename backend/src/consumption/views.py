from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from consumption.models import Consumption, Tariff, Area, User
from consumption.operations.get_number_of_users_by_area import get_number_of_users_by_area
from consumption.operations.get_user_consumption_by_time_of_day import get_user_consumption_by_time_of_day
from consumption.serializers import ConsumptionSerializer, TariffSerializer, AreaSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class ConsumptionViewSet(viewsets.ModelViewSet):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


@api_view(["GET"])
def number_of_users_by_area(request: Request) -> Response:
    return Response(data=get_number_of_users_by_area())


@api_view(["GET"])
def user_consumption_by_time_of_day(request: Request) -> Response:
    return Response(data=get_user_consumption_by_time_of_day())
