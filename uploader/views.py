from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from rest_framework import viewsets, parsers
from rest_framework.views import APIView
from .models import DropBox
from django.shortcuts import get_object_or_404
from .serializers import DropBoxSerializer
class DropBoxViewset(viewsets.ViewSet):
 
    def list(self,request):
        dropboxs = DropBox.objects.all()
        serializer = DropBoxSerializer(dropboxs,many=True)
        return Response(serializer.data)
       
    def create(self,request):
        serializer = DropBoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

    def retreive(self,request,pk = None):
        queryset = DropBox.objects.all()
        dropbox = get_object_or_404(queryset, pk = pk)
        serializer = DropBoxSerializer(data = dropbox)
        return Response(serializer.data)
    
    def update(self,request,pk = None):
        dropbox = DropBox.objects.get(pk = pk)
        serializer = DropBoxSerializer(dropbox,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DropBoxAPIView(APIView):

    def get(self,request):
        dropbox = DropBox.objects.all()
        serializer = DropBoxSerializer(dropbox, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DropBoxSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DropboxDetailAPIView(APIView):
    def get(self,request,id):
        try:
            dropbox = DropBox.objects.get(pk = id)
            serializer = DropBoxSerializer(dropbox)
            return Response(serializer.data)
        except DropBox.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        dropbox = DropBox.objects.get(pk = id)
        serializer = DropBoxSerializer(dropbox,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        dropbox = DropBox.objects.get(pk = id)
        dropbox.delete()
        return Response({"message": "delete success!"},status=status.HTTP_204_NO_CONTENT)



