from rest_framework import viewsets

from .models import Customers
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()  # Se obtiene todo el queryset de Customers
    serializer_class = CustomerSerializer  # Se utiliza el serializador definido
