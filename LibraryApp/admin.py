from django.contrib import admin
# Register your models here.
from LibraryApp.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'first_name', 'last_name', 'nickname')


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'title', 'category')


admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Edition)
admin.site.register(Publisher)
admin.site.register(Borrowing)
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Subscription)
admin.site.register(Payments)
