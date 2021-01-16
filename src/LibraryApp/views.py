from os.path import exists

from django.shortcuts import render, redirect

from math import ceil

from .models import Book, Author, Edition, User
from .forms import *

page_elements = 20

def index(request):
    return render(request, 'LibraryApp/index.html')

def login(request):
    warnings = []
    if request.method == 'POST':
        try:
            current_user = User.objects.get(name=request.POST['name'])
            if current_user.password.lower() == request.POST['password'].lower():
                request.session['user'] = current_user.user_id
                return redirect('browse')
        except User.DoesNotExist:
            pass
        warnings.append("Nieprawidłowa nazwa użytkownika lub hasło")
    return render(request, 'LibraryApp/login.html', {'warnings': warnings})

def logout(request):
    del request.session['user']
    return redirect('')

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
    return render(request, 'LibraryApp/browse.html', context=ctx)

def register(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    context = {'form': form}
    return render(request, 'LibraryApp/register.html', context)

def read(request):
    return render(request, 'LibraryApp/read.html')

def user(request):
    return render(request, 'LibraryApp/user.html')
