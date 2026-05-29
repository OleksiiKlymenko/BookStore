from django.shortcuts import render
from .models import Book, Category
from django.db.models import Q, Count, Avg, Sum, Max
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


def book_store_home(request):
    query = request.GET.get("search", "").strip()
    categories = Category.objects.annotate(books_count=Count("books"))

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query), stock__gt=0
        )
    else:
        books = Book.objects.filter(stock__gt=0)

    stats = Book.objects.aggregate(
        average_price=Avg("price"), total_stock=Sum("stock"), max_price=Max("price")
    )

    context = {"books": books, "categories": categories, "query": query, "stats": stats}

    return render(request, "catalog/books.html", context)


class BookListView(ListView):
    model = Book
    template_name = "catalog/bookslist.html"
    context_object_name = "bookslist"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get("search", "")
        price_max = self.request.GET.get("price_max", "")

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(description__icontains=search_query)
            )

        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search", "")
        context["price_max_value"] = self.request.GET.get("price_max", "")
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = "book"


class BookCreateView(CreateView):
    model = Book
    template_name = "catalog/book_form.html"
    fields = [
        "title",
        "author",
        "category",
        "price",
        "stock",
        "description",
    ]
    success_url = reverse_lazy("home")


class BookUpdateView(UpdateView):
    model = Book
    template_name = "catalog/book_form.html"
    fields = ["title", "author", "category", "price", "stock", "description"]
    success_url = reverse_lazy("home")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "catalog/book_confirm_delete.html"
    success_url = reverse_lazy("home")
