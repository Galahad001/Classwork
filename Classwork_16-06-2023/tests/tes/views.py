
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
    
@api_view(["GET", "POST"])
def api_posts(request):
    if request.method == 'GET':
        test = People.objects.all()
        serializer = TestsSer(test, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TestsSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_posts_detail(request, pk):
    p = People.objects.get(pk=pk)
    if request.method == 'GET':
        test = People.objects.get(pk=pk)
        serializer = TestsSer(test)
        return Response(serializer.data)
    elif request.method == "PUT" or request.method == "PATCH":
        serializer = TestsSer(p, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

def index(request):
    pass
# Create your views here.
