from django.contrib import admin

# Register your models here.
from .models import Book

class bookField (admin.ModelAdmin):
    list_display=('title','author','genre', 'published_year','isbn','publisher','pages','language','description','cover_image_url')

admin.site.register(Book,bookField)


