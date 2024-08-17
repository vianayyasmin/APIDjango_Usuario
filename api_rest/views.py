from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

from . import functions as fn

@api_view(['GET'])
def get_users(request):
    
    if request.method == 'GET':
        
        users = User.objects.all() #Pega todos os objetos no banco de dados User (retorna um queryset)
        
        serializer = UserSerializer(users, many=True) #Serializa os dados dos objeto em json (tem um parametro 'many' pq é um queryset)
        
        return Response(serializer.data) #Retorna o dado serializado
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):
    
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#CRUD
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    
    #Ler os dados
    
    if request.method == 'GET':
        
        try:
            if request.GET['user']: #Verifica se existe um parametro chamado 'user' 
                
                user_nickname = request.GET['user'] #Acha o parametro
                #A PK usada foi o nome de usuário porém poderia ser o id
                
                try:
                    user = User.objects.get(pk=user_nickname) #Pega o objeto no banco de dados
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user) #Serializa os dados do objeto em json
                return Response(serializer) #Retorna os dados serializados
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Criar os dados
    
    if request.method == 'POST':
        
        new_user = request.data
        
        serializer = UserSerializer(data=new_user)
        
        if serializer.is_valid(): #Verifica se os dados são válidos
            serializer.save() #Salva no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Editar os dados (PUT)
    
    if request.method == 'PUT':
        
        nickname = request.data['user_nickname']
        try:
            updated_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND) #Se você mudar o nome de usuário 
        
        print(request.data) 
        
        
        
        serializer = UserSerializer(updated_user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
        print('Resultado final ', fn.soma(1,2))

        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Deletar os dados (DELETE)
    
    if request.method == 'DELETE':

        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)










# def databaseEmDjango():
#    data = Usuario.objects.get(pk='usuario_apelido')  #OBJETO
    
#    data = Usuario.objects.filter(usuario_idade='17') #QUERYSET
    
#    data = Usuario.objects.exclude(usuario_idade='17')  #QUERYSET
    
#    data.save()
    
#    data.delete()
