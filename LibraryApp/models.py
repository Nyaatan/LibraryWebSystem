# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    nickname = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        # return f"{self.first_name}{' ' + self.nickname if self.nickname is not None else ''} {self.last_name}"
        return f"{self.author_id}"

    class Meta:
        managed = False
        db_table = 'Author'


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    category = models.ForeignKey('Category', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Book'


class Bookauthor(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'BookAuthor'


class Borrowing(models.Model):
    borrowing_id = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    isbn = models.ForeignKey('Edition', models.DO_NOTHING, db_column='isbn')
    user = models.ForeignKey('User', models.DO_NOTHING)

    def __str__(self):
        return f"{self.borrowing_id}"

    class Meta:
        managed = False
        db_table = 'Borrowing'


class Card(models.Model):
    card_id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=16)
    token = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.card_id}"

    class Meta:
        managed = False
        db_table = 'Card'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.category_id}"

    class Meta:
        managed = False
        db_table = 'Category'


class Edition(models.Model):
    isbn = models.BigIntegerField(primary_key=True)
    number = models.IntegerField(blank=True, null=True)
    page_count = models.IntegerField()
    date = models.DateField()
    book = models.ForeignKey(Book, models.DO_NOTHING)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING)

    def __str__(self):
        return f"{self.isbn}"

    class Meta:
        managed = False
        db_table = 'Edition'


class Payments(models.Model):
    payments_id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    def __str__(self):
        return f"{self.payments_id}"

    class Meta:
        managed = False
        db_table = 'Payments'


class Publisher(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.publisher_id}"

    class Meta:
        managed = False
        db_table = 'Publisher'


class Subscription(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=16)
    price = models.IntegerField()
    borrowing_count = models.IntegerField()

    def __str__(self):
        return f"{self.subscription_id}"

    class Meta:
        managed = False
        db_table = 'Subscription'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=16)
    email = models.CharField(unique=True, max_length=32)
    password = models.CharField(max_length=64, db_column='hash')
    borrowings_remaining = models.IntegerField()
    subscription = models.ForeignKey(Subscription, models.DO_NOTHING)
    card = models.ForeignKey(Card, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.user_id}"

    class Meta:
        managed = False
        db_table = 'User'
