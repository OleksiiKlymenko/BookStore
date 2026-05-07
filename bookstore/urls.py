from django.contrib import admin
from django.urls import path

from catalog.views import book_store_home

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', book_store_home, name='home')
]
