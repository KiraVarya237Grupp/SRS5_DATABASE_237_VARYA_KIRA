from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('stats/', views.stats_view, name='stats'),
    path('api/entry/<int:entry_id>/update/', views.api_update_status, name='api_update_status'),
    path('api/entry/<int:entry_id>/delete/', views.api_delete_entry, name='api_delete_entry'),
    path('update-status/<int:pk>/', views.update_status_view, name='update_status'),
    path('entry/<int:pk>/', views.entry_detail_view, name='entry_detail'),
]