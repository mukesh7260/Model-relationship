from django.shortcuts import render

from tryapp.models import *
from tryapp.serializers import *
from rest_framework.decorators import api_view 
from rest_framework.response import Response


@api_view(['GET'])
def porduct(request):
    prod = ProductMainModel.objects.all()
    serializer = ProductMainModelSerializer(prod,many=True) 
    return Response({'serilai':serializer.data})
   


@api_view(['GET'])
def porductt(request,pk):
    prod = ProductMainModel.objects.get(id = pk)
    serializer = ProductMainModelSerializer(prod) 
    return Response({'serilai':serializer.data})




