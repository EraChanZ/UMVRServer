from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'key':'value'
        }
        return Response(data)

""" def test(request):
    data = {
        'key':'value'
    }
    return JsonResponse(data) """