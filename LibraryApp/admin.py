from django.contrib import admin
# Register your models here.
from LibraryApp.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'first_name', 'last_name', 'nickname')


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'title', 'category')


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('borrowing_id', 'start_date', 'end_date',
                    'isbn', 'user')


class CardAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'number', 'token')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'description')


class EditionAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'number', 'page_count', 'date', 'book',
                    'publisher')


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('payments_id', 'amount', 'date', 'user')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('publisher_id', 'name')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription_id', 'name', 'price',
                    'borrowing_count')


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'hash',
                    'borrowings_remaining', 'subscription',
                    'card')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Borrowing, BorrowingAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Payments, PaymentsAdmin)
