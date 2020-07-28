#URLs de Alquiler de Maquinaria
from django.urls import path, include
#Vista
from .views import AlquilerViewSet
#Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('alquileres', AlquilerViewSet, basename = 'alquileres')

urlpatterns = [
    path('', include(router.urls)),
]