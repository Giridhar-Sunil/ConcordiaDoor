from django.contrib import admin
from .models import Textbook

@admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'course_code', 'year', 'edition', 'availability')

    
