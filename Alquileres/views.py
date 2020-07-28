#Vistas de Alquiler de Maquinaria
from rest_framework import status
from rest_framework.response import Response
#Viewset
from rest_framework import viewsets
#Modelo
from .models import Alquiler
#Serializador
from .serializer import AlquilerSerializer
#Permisos
from .permissions import IsOwner
from rest_framework.permissions import IsAdminUser #también está aquí

class AlquilerViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer
    permission_classes = [IsAdminUser, IsOwner]