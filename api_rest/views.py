from django.shortcuts import render
from django.http import HttpResponse, JsonResponse  

from rest_framework.decorators import api_view
from rest_framework.response import Response        
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json


@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_by_nick(request,nick):

    try: 
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)   

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':

        # aqui ele tenta achar a chave user dentra da requisição
        try:
           if request.GET['user']:
            # Procure na URL algo que venha depois do sinal de igual de uma etiqueta chamada user 
            user_nickname = request.GET['user']
            try:
                # verifica se na classe User no banco de dados existe um user com esse nickname
                user = User.objects.get(pk=user_nickname)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
               
            serializer = UserSerializer(user)
            return Response(serializer.data)
           
           else:
               return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
           return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'POST':

        new_user = request.data

        serializar = UserSerializer(data=new_user)

        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':

        nickname = request.data ['user_nickname']

        try:
            update_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            print(request.data)

        serializer = UserSerializer(update_user, data=request.data)

        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        
        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname']) 
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

           
            

      