from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),  # <-- Подключаем в корень '' вместо 'catalog/'
]