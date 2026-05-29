from django.contrib import admin
from django.urls import path
from catalog import views

from catalog.views import book_store_home

app_name = "catalog"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", book_store_home, name="home"),
    path("listhome/", views.BookListView.as_view(), name="listhome"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("book/add/", views.BookCreateView.as_view(), name="book_create"),
    path("book/<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_edit"),
    path(
        "book/<int:pk>/delete/",
        views.BookDeleteView.as_view(),
        name="book_delete",
    ),
]
