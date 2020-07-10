from django.shortcuts import render
from rest_framework import viewsets, status
from account.models import Account
from rest_framework.decorators import api_view, authentication_classes, action, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from account.api.serializers import RegistrationSerializer, AccountSerializer, AccountUpdateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully did a thing"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = AccountUpdateSerializer

        return serializer_class
    
    def update(self, request, *args, **kwargs):
        if request.method != 'PUT':
            return Response("Only PUT allowed", status=status.HTTP_400_BAD_REQUEST)
        partial = True 
        user = request.user
        serializer = self.get_serializer(user, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_data(self, request, *args, **kwargs):
        user = request.user
        serializer = AccountSerializer(user)
        return Response(serializer.data)
    
