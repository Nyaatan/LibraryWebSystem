from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'libraryApp/index.html')


def login(request):
    return render(request, 'libraryApp/login.html')


def browse(request):
    return render(request, 'libraryApp/browse.html')


def register(request):
    return render(request, 'libraryApp/register.html')


def read(request):
    return render(request, 'libraryApp/read.html')


def user(request):
    return render(request, 'libraryApp/user.html')
