from django.urls import path
from .views import  NewUser, GetUsers, Login

urlpatterns = [
    path('register', NewUser.as_view()),
    path('users', GetUsers.as_view()),
    path('login', Login.as_view())
]