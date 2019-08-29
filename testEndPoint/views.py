from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from testEndPoint.models import TestEndpoint
from testEndPoint.serializers import SnippetSerializer


@api_view(['GET','POST'])
def s_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        s = TestEndpoint.objects.all()
        serializer = SnippetSerializer(s, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def s_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        s = TestEndpoint.objects.get(pk=pk)
    except s.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(s)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        s.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
