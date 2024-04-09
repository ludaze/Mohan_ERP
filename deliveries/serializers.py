from rest_framework import serializers
from deliveries.models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = delivery
        fields = '__all__'