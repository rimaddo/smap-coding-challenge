from rest_framework import serializers

from consumption.models import User, Area, Tariff, Consumption


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = "__all__"


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = "__all__"

