from django.contrib import admin
from django.urls import include, path  # Додали include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Підключаємо всі маршрути з додатка catalog і реєструємо для них namespace
    path("", include("catalog.urls")),
]
