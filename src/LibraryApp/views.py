import os

from django.core.exceptions import PermissionDenied
from django.http import *
from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime, timedelta

from math import ceil

from .models import Author, Edition, User, Borrowing
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
        sort = 'book__bookauthor__author__last_name'
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
    elif sort == 'book__bookauthor__author__last_name':
        editions = (Edition.objects.filter(book__bookauthor__author__first_name__icontains=string) |
                    Edition.objects.filter(book__bookauthor__author__last_name__icontains=string) |
                    Edition.objects.filter(book__bookauthor__author__nickname__icontains=string)).order_by(sort)[
                   (page - 1) * page_elements:
                   min(page * page_elements,
                       Edition.objects.count())]
    else:
        editions = Edition.objects.order_by(sort)
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
                'isbn': edition.isbn,
                'description': open(f'LibraryApp/static/LibraryApp/books/descs/{edition.isbn}.txt', encoding='UTF-8').read()
                if os.path.exists(
                    f'LibraryApp/static/LibraryApp/books/descs/{edition.isbn}.txt')
                else open('LibraryApp/static/LibraryApp/books/descs/default.txt', encoding='UTF-8').read(),
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
    reader_id = request.session.get('user', None)
    if (isbn < 0) or (reader_id is None):
        raise PermissionDenied
    context['isbn'] = isbn
    user = User.objects.get(user_id=request.session['user'])
    if user.borrowings_remaining > 0:
        if len(Borrowing.objects.filter(user_id=user.user_id, isbn=isbn)) == 0:
            borrow = Borrowing(start_date=datetime.today(), end_date=datetime.today() + timedelta(days=30),
                                isbn=Edition.objects.get(isbn=isbn), user_id=user.user_id,
                                borrowing_id=Borrowing.objects.count())
            borrow.save()
            user.borrowings_remaining -= 1
            user.save()
        try:
            book_data = Edition.objects.get(isbn=isbn)
            context['title'] = book_data.book.title
        except Edition.DoesNotExist:
            pass
    else:
        raise PermissionDenied
    return render(request, 'LibraryApp/read.html', context)


def user(request):
    user = User.objects.get(user_id=request.session['user'])
    form = SignUpForm()
    if request.method == 'POST':
        if request.POST['type'] == 'u':
            data = request.POST
            name = data['name']
            email = data['email']
            password = data['password']
            if name != '':
                user.name = name
            if email != '':
                user.email = email
            if password != '':
                user.password = password
            user.save()
        elif request.POST['type'] == 's':
            sub = Subscription.objects.get(subscription_id=int(request.POST['subscription']))
            user.borrowings_remaining = sub.borrowing_count - (
                        user.subscription.borrowing_count - user.borrowings_remaining)
            user.subscription = sub
            user.save()
    user.borrowings_remaining = max(user.borrowings_remaining, 0)
    ctx = {
        'user': user,
        'borrowings': Borrowing.objects.filter(user_id=user.user_id),
        'form': form,
        'subscriptions': Subscription.objects.all()
    }
    return render(request, 'LibraryApp/user.html', context=ctx)


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
        # return HttpResponseBadRequest()
        file_path = os.path.join(location, "default" + extension)
    with open(file_path, 'rb') as file:
        data = file.read()
    response = HttpResponse(content_type="application/octet-stream")
    response['Content-Description'] = 'File Transfer'
    response['Cache-Control'] = 'must-revalidate'
    response['Content-Length'] = len(data)
    response.write(data)
    return response
