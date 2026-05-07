from django.shortcuts import render
from .models import Book, Category
from django.db.models import Q, Count, Avg, Sum, Max

def book_store_home(request):
    query = request.GET.get('search', '').strip()
    categories = Category.objects.annotate(books_count=Count('books'))

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query),
            stock__gt=0
        )
    else:
        books = Book.objects.filter(stock__gt=0)

    stats = Book.objects.aggregate(
        average_price=Avg('price'),
        total_stock=Sum('stock'),
        max_price=Max('price')
    )

    context = {
        'books': books,
        'categories': categories,
        'query': query,
        'stats': stats
    }

    return render(request, 'catalog/books.html', context)

