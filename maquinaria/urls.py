#URLs para Maquinaria
from django.urls import path, include
#Vista
from .views import MaquinariaViewSet
#Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('maquinaria', MaquinariaViewSet, basename = 'maquinaria')

urlpatterns = [
    path('', include(router.urls)),
]