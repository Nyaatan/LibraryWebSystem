import random
from datetime import datetime

from numpy.random import randint as uniform

from faker import Faker
from settings import *

class Author:
    def __init__(self):
        self.id = None
        self.last_name = None
        self.locale = None
        self.nickname = None
        self.first_name = None
        self.id = 0

    @staticmethod
    def random(loc=locales, id=0):
        locale = random.choices(loc)
        faker = Faker(locale)
        author = Author()
        author.id = id
        author.locale = locale
        author.first_name, author.last_name = faker.first_name(), faker.last_name()
        author.nickname = f" '{faker.word().capitalize()}'" if uniform(1, 10) == 1 else 'null'
        return author

    def query(self):
        return f'INSERT INTO "Author"(author_id, first_name, last_name, nickname) VALUES ({self.id},  ' \
            f"'{self.first_name}', '{self.last_name}', {self.nickname});"

    def __str__(self):
        return f"{self.id} {self.first_name}{self.nickname} {self.last_name}"

    __repr__ = __str__


class Category:
    def __init__(self):
        self.description = None
        self.name = None
        self.id = 0

    @staticmethod
    def random(name=None):
        faker = Faker('pl')
        cat = Category()
        cat.name = name
        cat.description = faker.text(16)
        return cat

    def query(self):
        return f'INSERT INTO "Category"(category_id, name, description) VALUES ({self.id},  ' \
            f"'{self.name}', '{self.description}');"

    def __str__(self):
        return f"{self.id} {self.name}"

    __repr__ = __str__


class Publisher:
    def __init__(self):
        self.name = None
        self.id = 0

    @staticmethod
    def random(loc=locales):
        faker = Faker(loc)
        pub = Publisher()
        pub.name = faker.company()
        return pub

    def query(self):
        return f'INSERT INTO "Publisher"(publisher_id, name) VALUES ({self.id}, ' \
            f"'{self.name}');"

    def __str__(self):
        return f"{self.id} {self.name}"

    __repr__ = __str__


class Book:
    def __init__(self):
        self.publisher = None
        self.title = None
        self.category = None
        self.subauthors = None
        self.author = None
        self.id = 0

    @staticmethod
    def random(loc=locales, author=None, subauthors=None, cateory=None, publisher=None):
        if author is None:
            author = Author.random(loc)

        faker = Faker(author.locale)

        book = Book()
        book.author = author
        book.subauthors = subauthors
        book.locale = author.locale
        book.title = faker.sentence(4).replace('.', '')
        book.category = cateory
        return book

    def query(self):
        string = f'INSERT INTO "Book"(book_id, title, category_id) VALUES ({self.id}, ' \
            f"'{self.title}', {self.category.id});"
        string += f"\n" + f'INSERT INTO "BookAuthor"(book_id, author_id) VALUES ({self.id}, {self.author.id});'
        if self.subauthors is not None:
            for subauth in self.subauthors:
                string += f"\n" + f'INSERT INTO "BookAuthor"(book_id, author_id) VALUES ({self.id}, {subauth.id});'
        return string

    def __str__(self):
        return f"{self.id} {self.author}" \
            f"{', ' + ','.join([str(i) for i in self.subauthors]) if self.subauthors is not None else ''} " \
            f"'{self.title}', {self.category}, {self.publisher}"

    __repr__ = __str__


class Edition:
    def __init__(self):
        self.page_count = None
        self.book = None
        self.isbn = None
        self.date = None
        self.publisher = None
        self.number = None

    @staticmethod
    def random(loc=locales, book=None, publisher=None):
        faker = Faker(loc)
        ed = Edition()
        ed.number = uniform(1, 7)
        ed.page_count = uniform(100, 1000)
        ed.date = faker.date()
        ed.isbn = faker.isbn13().replace('-', '')
        ed.book = book
        ed.publisher = publisher
        return ed

    def query(self):
        return f'INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES({self.isbn},' \
            f" {self.number}, {self.page_count}, '{self.date}', {self.book.id}, {self.publisher.id});"

    def __str__(self):
        return f"'ISBN: {self.isbn}, {self.book.title}' Edition: {self.number}, Pages: {self.page_count}, Publisher: {self.publisher}, " \
            f"Date: {self.date} "

    __repr__ = __str__


class Card:
    def __init__(self):
        self.number = None
        self.token = None
        self.id = 0

    @staticmethod
    def random(loc=locales):
        faker = Faker(loc)
        card = Card()
        card.number = f'{"*" * 12}{faker.credit_card_number()[-4:]}'
        card.token = faker.binary(length=16)
        return card

    def query(self):
        return f'INSERT INTO "Card"(card_id, number, token) VALUES (' \
            f"{self.id}, '{self.number}', '{str(hex(int.from_bytes(self.token, byteorder='big')))[2:]}');"

    def __str__(self):
        return f"{self.id} {self.number} {self.token}"

    __repr__ = __str__


class Subscription:
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price
        self.id = 0

    def query(self):
        return f'INSERT INTO "Subscription"(subscription_id, name, price, borrowing_count) VALUES({self.id}, ' \
            f"'{self.name}', {self.price}, {self.count});"

    def __str__(self):
        return f"{self.id} {self.name} {self.count} {self.price}"

    __repr__ = __str__


class User:
    def __init__(self):
        self.name = None
        self.email = None
        self.hash = None
        self.subscription = None
        self.borrowings_remaining = None
        self.card = None
        self.id = 0

    @staticmethod
    def random(loc=locales, subscription=None, card=None):
        faker = Faker(locales)
        user = User()
        user.name = faker.word()
        user.email = faker.email()
        user.hash = faker.binary(length=32)
        user.subscription = subscription
        user.borrowings_remaining = uniform(0, subscription.count)
        user.card = card
        return user

    def query(self):
        return f'INSERT INTO "User"(user_id, name, email, hash, borrowings_remaining, subscription_id, card_id) VALUES(' \
            f"{self.id}, '{self.name}', '{self.email}', '{str(hex(int.from_bytes(self.hash, byteorder='big')))[2:]}'," \
            f" {self.borrowings_remaining}, " \
            f"{self.subscription.id}, {self.card.id});"

    def __str__(self):
        return f'{self.id} {self.name} {self.email} {self.hash} {self.subscription} {self.borrowings_remaining} {self.card}'

    __repr__ = __str__


class Payment:
    def __init__(self):
        self.date = None
        self.user = None
        self.ammount = None
        self.id = 0

    @staticmethod
    def random(loc=locales, user=None):
        faker = Faker(loc)
        payment = Payment()
        payment.ammount = user.subscription.price
        payment.date = faker.date_between(datetime.now().replace(day=1))
        payment.user = user
        return payment

    def query(self):
        return f'INSERT INTO "Payments"(payments_id, amount, date, user_id) VALUES({self.id}, {self.ammount}, ' \
            f"'{self.date}', {self.user.id});"

    def __str__(self):
        return f"{self.id} {self.date} {self.user.id} {self.ammount}"

    __repr__ = __str__


class Borrowing:
    def __init__(self):
        self.user = None
        self.edition = None
        self.end_date = None
        self.start_date = None
        self.id = 0

    @staticmethod
    def random(loc=locales, user=None, edition=None):
        faker = Faker(loc)
        bor = Borrowing()
        bor.user = user
        bor.edition = edition
        bor.start_date = faker.date_between_dates(datetime.now().replace(day=1), datetime.now())
        bor.end_date = faker.date_between_dates(bor.start_date, datetime.now())
        return bor

    def query(self):
        return f'INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES ({self.id}, ' \
            f"'{self.start_date}', '{self.end_date}', {self.edition.isbn}, {self.user.id});"

    def __str__(self):
        return f"{self.id} {self.user.name} {self.edition.isbn} {self.start_date} {self.end_date}"

    __repr__ = __str__
