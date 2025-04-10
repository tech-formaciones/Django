from rest_framework import serializers
from .models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'  # Incluye todos los campos del modelo
