from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


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