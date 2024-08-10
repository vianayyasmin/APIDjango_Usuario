from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializador

import json

@api_view(['GET'])
def get_usuarios(request):
    
    if request.method == 'GET':
        
        usuarios = Usuario.objects.all()
        
        serializador = UsuarioSerializador(usuarios, many=True)
        
        return Response(serializador.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)














# def databaseEmDjango():
#    data = Usuario.objects.get(pk='usuario_apelido')  #OBJETO
    
#    data = Usuario.objects.filter(usuario_idade='17') #QUERYSET
    
#    data = Usuario.objects.exclude(usuario_idade='17')  #QUERYSET
    
#    data.save()
    
#    data.delete()
