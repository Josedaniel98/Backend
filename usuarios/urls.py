from django.urls import path, include
from rest_framework.routers import DefaultRouter
#Vistas
from .views import AdminViewset, UsuarioViewset, LoginView

router = DefaultRouter()
router.register('usuarios/admins', AdminViewset, basename='admin')
router.register('usuarios/clientes', UsuarioViewset, basename='cliente')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login')
]
