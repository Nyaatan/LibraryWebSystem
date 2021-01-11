from os.path import exists

from django.shortcuts import render, redirect

# Create your views here.
from math import ceil

from LibraryApp.models import Book, Author, Edition, User
from .forms import LoginForm

page_elements = 20


def index(request):
    return render(request, 'libraryApp/index.html')


def login(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        users_list = User.objects.order_by('user_id')
        if users_list.filter(name=request.POST['name'], password=request.POST['password']).exists():
            return redirect('browse')
    context = {'form': form}
    return render(request, 'libraryApp/login.html', context)


def browse(request):
    try:
        page = min(max(int(request.GET.get('p', 1)), 1), ceil(Edition.objects.count() / 20))
    except (ValueError, AttributeError):
        page = 1

    sort = request.GET.get('sort', 'n')
    if sort == 'n':
        sort = 'book__title'
    elif sort == 'a':
        sort = 'book__bookauthor__author__first_name'
    order = request.GET.get('order', 'a')
    if order == 'a':
        pass
    elif order == 'd':
        sort = f'-{sort}'
    string = request.GET.get('search', '')
    if sort == 'book__title':
        editions = Edition.objects.filter(book__title__icontains=string).order_by(sort)[(page - 1) * page_elements:
                                                                                        min(page * page_elements,
                                                                                            Edition.objects.count())]
    elif sort == 'book__bookauthor__author__first_name':
        editions = (Edition.objects.filter(book__bookauthor__author__first_name__icontains=string) |
                    Edition.objects.filter(book__bookauthor__author__last_name__icontains=string) |
                    Edition.objects.filter(book__bookauthor__author__nickname__icontains=string)).order_by(sort)[
                   (page - 1) * page_elements:
                   min(page * page_elements,
                       Edition.objects.count())]
    ctx = {
        'books': {
            edition.book: {
                'authors': Author.objects.filter(bookauthor__book__book_id=edition.book.book_id).all(),
                'cover': f'LibraryApp/books/covers/{edition.isbn}.jpg'
                if exists(
                    f'LibraryApp/static/LibraryApp/books/covers/{edition.isbn}.jpg') else 'LibraryApp/books/covers/default.jpg',
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
