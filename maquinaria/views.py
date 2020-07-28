  
# Vistas de Maquinaria
from rest_framework import viewsets
#Autenticación
from rest_framework.permissions import IsAuthenticated, IsAdminUser #también está aquí
#Serializador
from .serializer import MaquinariaSerializer
#Modelo
from .models import Maquinaria

class MaquinariaViewSet(viewsets.ModelViewSet):
    queryset = Maquinaria.objects.all()
    serializer_class = MaquinariaSerializer
    permissions_classes = [IsAdminUser]