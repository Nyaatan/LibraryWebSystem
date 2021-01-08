from os.path import exists

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from math import ceil

from LibraryApp.models import Book, Author, Edition

page_elements = 20


def index(request):
    return render(request, 'libraryApp/index.html')


def login(request):
    return render(request, 'libraryApp/login.html')


def browse(request):
    ctx = {}
    try:
        page = min(max(int(request.GET.get('p', 1)), 1), ceil(Edition.objects.count()/20))
    except ValueError:
        page = 0

    editions = Edition.objects.all().order_by('book__title')[(page - 1) * page_elements:
                                                             min(page * page_elements, Edition.objects.count())]
    ctx = {
        'books': {
            edition.book: {
                'authors': Author.objects.filter(bookauthor__book__book_id=edition.book.book_id).all(),
                'cover': f'LibraryApp/books/covers/{edition.isbn}.jpg'
                if exists(f'LibraryApp/books/covers/{edition.isbn}.jpg') else 'LibraryApp/books/covers/default.jpg',
                'isbn': edition.isbn
            } for edition in editions
        },
        'page': page,
    }
    return render(request, 'libraryApp/browse.html', context=ctx)


def register(request):
    return render(request, 'libraryApp/register.html')


def read(request):
    return render(request, 'libraryApp/read.html')


def user(request):
    return render(request, 'libraryApp/user.html')
