from django.shortcuts import render
from rest_framework.response import Response
from .serializers import OssoSerializer
from rest_framework.decorators import api_view
from .models import Osso
from rest_framework import status


@api_view(['GET'])
def obter_osso(request):
    osso = Osso.objects.first()

    if osso:

        serializer = OssoSerializer(osso)
        
        return Response(serializer.data, status=200)
    
    else:
        return Response(serializer.errors ,{
            "Osso não encontrado..."
        }, status=404)
    
@api_view(['POST'])
def criar_osso(request):

    novo_osso = request.data

    serializer = OssoSerializer(data = novo_osso)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=200)
    
    else:
        return Response(serializer.errors, status=404)
    
@api_view(['DELETE'])
def deletar_osso(request,pk):
    
    try:
        
        osso = Osso.objects.get(pk=pk)

        osso.delete()

        return Response({"mensagem" : "Osso deletado com sucesso"}, status=200)
    
    except Osso.DoesNotExist:

        return Response({"mensagem" : "Osso não encontrado no banco de dados!"}, status=404)
    
@api_view(['PUT'])
def atualizar_osso(request,pk):
    
    try:
        
        osso = Osso.objects.get(pk=pk)

        osso.nome = request.data.get('nome', osso.nome)
        osso.objeto3D = request.data.get('objeto3D', osso.objeto3D)
        osso.descricao = request.data.get('descricao', osso.descricao)

        osso.save()

        return Response({"mensagem" : "Osso atualizado com sucesso!"}, status=200)

    except Osso.DoesNotExist:

        return Response({"mensagem" : "Osso não encontrado no banco de dados!"}, status=404)
    
@api_view(['GET'])
def obter_todos(request):

        osso = Osso.objects.all();
        serializer = OssoSerializer(osso, many=True)
        
        return Response(serializer.data)


@api_view(['POST'])
def procurar_osso(request):

    nome = request.data.get("nome");

    if not nome:
        
        return Response({"erro": "Por favor, forneça um nome para busca."}, status=400)
        
    try:
        
        osso = Osso.objects.get(nome__iexact=nome);
        serializer = OssoSerializer(osso);
        return Response(serializer.data, status=200);

    except Osso.DoesNotExist:

        return Response({"Erro": "Esse osso não existe no banco de Dados!"}, status=404);