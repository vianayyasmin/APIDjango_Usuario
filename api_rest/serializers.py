from rest_framework import serializers

from .models import Usuario



class UsuarioSerializador(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
