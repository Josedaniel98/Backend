from rest_framework import serializers
#Modelos
from .models import usuario
#Token
from rest_framework.authtoken.models import Token

class UsuarioSerializer (serializers.ModelSerializer):
    """
        Serializador del usuario
    """
    class Meta:
        model = usuario
        fields = ['id', 'username', 'email', 'password', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = usuario(
            username = validated_data['username'],
            email = validated_data['email'],
            is_staff = validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()

        Token.objects.create(user = user)

        return user
        