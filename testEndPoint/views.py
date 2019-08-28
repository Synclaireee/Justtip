from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from testEndPoint.models import TestEndpoint
from testEndPoint.serializers import SnippetSerializer


@csrf_exempt
def s_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        s = TestEndpoint.objects.all()
        serializer = SnippetSerializer(s, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def s_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        s = TestEndpoint.objects.get(pk=pk)
    except s.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(s)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(s, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        s.delete()
        return HttpResponse(status=204)