  
#Serializadores de Maquinaria
from rest_framework import serializers
#Modelos
from .models import Maquinaria

class MaquinariaSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Maquinaria
        fields = '__all__'