from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, TorneoSerializer, ParticipanteSerializer, PartidoSerializer
from .models import User, Torneo, Participante, Partido
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class NewUser(APIView):
    serializer_class = UserSerializer
    def post(self, req, format=None):
        
        # print(email)
        # print(username)
        serializer = self.serializer_class(data=req.data)
        if serializer.is_valid():
            username = req.data.get('username')
            password = req.data.get('password')
            email = req.data.get('email')
            user = User(username=username, password=password, email=email)
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class GetUsers(APIView):
    serializer_class = UserSerializer
    def get(self, req, format=None):
        users = User.objects.all()
        return Response(users.values(), status=status.HTTP_200_OK)

class Login(APIView):
    serializer_class = UserSerializer
    def post(self, req, format=None):
        print(req.data)
        password = req.data.get('password')
        email = req.data.get('email')
        user = User.objects.get(email=email)
        # data = UserSerializer(user[0]).data
        print(user)
        

class UserView(APIView):
    pass

class TorneoView(APIView):
    pass

class ParticipanteView(APIView):
    pass

class PartidoView(APIView):
    pass