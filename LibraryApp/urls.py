from django.urls import path

from LibraryApp.views import *

urlpatterns = [
    path('index', index),
    path('', index),
]
