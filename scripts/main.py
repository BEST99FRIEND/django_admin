from main.models import Book, Author

def run():
    data = Book.objects.select_related('author').all()
    for book in data:
        print(f"Title: {book.title}, Author: {book.author.name}, Published Date: {book.published_date}")
    print(f"Hello, Django! Total Books: {data.count()}")