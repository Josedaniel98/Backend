#Permisos de RF
from rest_framework import permissions

#Esta sería una clase base de Permisos
class IsOwner(permissions.BasePermission):
    message = "No es propietario."
    
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS: #Si la petición es de GET, OPTIONS o HEAD
            return True
        return request.user == obj.owner #Hace la comparación de si el usuario requisitante es el propietario para hacer POST, PUT, PATCH...