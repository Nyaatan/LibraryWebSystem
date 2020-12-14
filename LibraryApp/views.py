from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'polls/index.html')


def login(request):
    return render(request, 'polls/login.html')


def browse(request):
    return render(request, 'polls/browse.html')


def register(request):
    return render(request, 'polls/register.html')


def read(request):
    return render(request, 'polls/read.html')


def user(request):
    return render(request, 'polls/user.html')
