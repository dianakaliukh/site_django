from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('catalog/', views.catalog),
    path('catalog/<int:category_id>/', views.products_by_category),
    path('contacts/', views.contacts),
]