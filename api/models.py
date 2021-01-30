from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Torneo.objects.filter(code=code).count() == 0:
            break

    return code


# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=100, null=False)
    email = models.EmailField(max_lenght=200, null=False)
    password = models.TextField(max_length=200, null=False)

class Torneo(models.Model):
    accessId = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Participante(models.Model):
    name = models.CharField(max_length=200, default="", null=False)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

class Partido(models.Model):
    resultado = models.BooleanField(null=False)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
