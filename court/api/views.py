from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, status
from account.models import Account
from rest_framework.decorators import api_view, authentication_classes, action, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from court.models import Court
from .serializers import CourtSerializer, CourtSerializerUpdate
import difflib

class CourtViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method in ['PUT', 'GET']:
            serializer_class = CourtSerializerUpdate

        return serializer_class

    def perform_create(self, serializer):
        user = None
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
        serializer.save(landlord=user)

    def update(self, request, pk=None, *args, **kwargs):
        obj = get_object_or_404(self.queryset, pk=pk)
        if obj.landlord == request.user:
            serializer = self.get_serializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid data'})
        else:
            return Response({'error': 'You are not landlord of this court'})
    
    @action(detail=False, methods=['get'])
    def my_courts(self, request):
        filtered = self.queryset.filter(landlord = request.user)
        serializer = self.get_serializer(filtered, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def suggestions(self, request):
        if request.query_params.get("query"):
            query = request.query_params.get("query")
            allnames = list(map(lambda a: a["name"], self.queryset.values('name')))
            matches = list(map(lambda a: {"text":a, "type":"court_name"}, difflib.get_close_matches(query, allnames, n = 10, cutoff = 0.0)))
            return Response({'suggestions': matches})
        else:
            return Response({'error': 'No query param specified'})