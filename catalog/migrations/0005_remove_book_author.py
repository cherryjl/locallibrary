from django.db import migrations

def authorize_books(apps, schema_editor):
    # "author-ize" get it X-D
    Author = apps.get_model("catalog", "Author")
    Book = apps.get_model("catalog", "Book")
    BookAuthor = apps.get_model("catalog", "BookAuthor")

    # Loop through all books and create a BookAuthor record using the old author field
    for book in Book.objects.all():
        if book.author:
            BookAuthor.objects.create(
                book=book,
                author=book.author,
                author_order=1
            )

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookauthor_book_authors'), # Leave whatever django auto-generated here
    ]

    operations = [
        # ADD THIS LINE FIRST so the data is saved before the field is deleted
        migrations.RunPython(authorize_books),
        
        # Django's auto-generated operation to remove the field will be below it
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]