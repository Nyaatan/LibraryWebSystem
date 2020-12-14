from django.urls import path

from LibraryApp.views import *

urlpatterns = [
    path('index', index),
    path('', index),
    path('login', login),
    path('register', register),
    path('user', user),
    path('read', read),
    path('browse', browse),
]
