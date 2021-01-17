import os

from django.http import *
from django.shortcuts import render, redirect
from django.conf import settings

from math import ceil

from .models import Author, Edition, User
from .forms import *

page_elements = 20

books_location = os.path.join(settings.BOOKS_DIR, "files")
book_descs_location = os.path.join(settings.BOOKS_DIR, "descs")
book_covers_location = os.path.join(settings.BOOKS_DIR, "covers")

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
                # do okładek pownien być używany osobny endpoint z js'a ładowane
                # czyli nie ze 'static' jak jest teraz
                # ale nie ma na to czasu :(
                if os.path.exists(
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
    context = {}
    isbn = int(request.GET.get('isbn', '-1'))
    if isbn > 0:
        context['isbn'] = isbn
        try:
            book_data = Edition.objects.get(isbn=isbn)
            context['title'] = book_data.book.title
        except Edition.DoesNotExist:
            pass
    return render(request, 'LibraryApp/read.html', context)

def user(request):
    return render(request, 'LibraryApp/user.html')

def get_book_stream(request):
    isbn = request.GET.get('isbn', None)
    return _create_book_data_response(isbn, books_location, ".pdf")

def get_book_desc(request):
    isbn = request.GET.get('isbn', None)
    return _create_book_data_response(isbn, book_descs_location, ".txt")

def get_book_cover(request):
    isbn = request.GET.get('isbn', None)
    return _create_book_data_response(isbn, book_covers_location, ".jpg")

def _create_book_data_response(book_isbn, location, extension):
    if book_isbn is None:
        return HttpResponseBadRequest()
    file_path = os.path.join(location, book_isbn + extension)
    if not os.path.isfile(file_path):
        #return HttpResponseBadRequest()
        file_path = os.path.join(location, "default" + extension)
    with open(file_path, 'rb') as file:
        data = file.read()
    response = HttpResponse(content_type="application/octet-stream")
    response['Content-Description'] = 'File Transfer'
    response['Cache-Control'] = 'must-revalidate'
    response['Content-Length'] = len(data)
    response.write(data)
    return response
