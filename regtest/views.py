from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from regtest.models import UserTest
from regtest.serializers import UserSerializer
from django.http import Http404


class R_List(APIView):
    def get(self,request, format=None):
        s = UserTest.objects.all()
        serializer = UserSerializer(s, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class R_Detail(APIView):
    def get_object(self,pk):
        try:
            return UserTest.objects.get(pk=pk)
        except UserTest.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        serializer = UserSerializer(s)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        serializer = UserSerializer(s, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)