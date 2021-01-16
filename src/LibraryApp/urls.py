from django.urls import path

from LibraryApp.views import *

urlpatterns = [
    path('', index, name=''),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('user/', user, name='user'),
    path('read/', read, name='read'),
    path('browse/', browse, name='browse'),
]