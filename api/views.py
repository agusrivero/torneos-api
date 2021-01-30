from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, TorneoSerializer, ParticipanteSerializer, PartidoSerializer
from .models import User, Torneo, Participante, Partido
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserView(APIView):
    pass

class TorneoView(APIView):
    pass

class ParticipanteView(APIView):
    pass

class PartidoView(APIView):
    pass