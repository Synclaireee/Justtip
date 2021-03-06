from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from testEndPoint.models import TestEndpoint
from testEndPoint.serializers import SnippetSerializer
from django.http import Http404


class S_List(APIView):
    def get(self,request, format=None):
        s = TestEndpoint.objects.all()
        serializer = SnippetSerializer(s, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class S_Detail(APIView):
    def get_object(self,pk):
        try:
            return TestEndpoint.objects.get(pk=pk)
        except TestEndpoint.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        s = self.get_object(pk)
        serializer = SnippetSerializer(s)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        s = self.get_object(pk)
        serializer = SnippetSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        s = self.get_object(pk)
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)