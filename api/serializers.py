from rest_framework import serializers
from .models import User, Torneo, Participante, Partido

class UserSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'username', 'email', 'password')

class TorneoSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'accessId', 'owner')

class ParticipanteSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'name', 'torneo')

class PartidoSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'resultado', 'participante')