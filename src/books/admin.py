from django.contrib import admin
from .models import book, BookTitle

# Register your models here.

admin.site.register(book)
admin.site.register(BookTitle)