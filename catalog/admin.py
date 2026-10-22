from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language, BookAuthor

# Standalone model registrations
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookAuthor)

# Inlines
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1

# Define the admin classes using decorators
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookAuthorInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre') 
    inlines = [BookAuthorInline, BooksInstanceInline] 

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )