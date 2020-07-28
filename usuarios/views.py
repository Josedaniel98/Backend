#Serializador
from .serializer import UsuarioSerializer
#Modelo
from .models import usuario
#Autenticación
from django.contrib.auth import authenticate
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated
#Vistas
from rest_framework import viewsets
from rest_framework.views import APIView
#Respuesta de Servidor
from rest_framework.response import Response
from rest_framework import status

class AdminViewset(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
    model = usuario
    permission_classes = []

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
    model = usuario
    permission_classes = [IsAdminUser]

class LoginView(APIView):
    permission_classes = []
    def post (self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username = username, password = password)
        
        if user:
            return Response(
                {'token': user.auth_token.key}
            )
        else:
            return Response(
                {'error': 'Credenciales inválidas. Inicie sesión.'},
                status= status.HTTP_400_BAD_REQUEST
            )