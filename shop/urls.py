from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('products/sort/<slug:sort_slug>', views.product_list, name='product_list_by_sort'),
    path('products/<slug:category_slug>/sort/<slug:sort_slug>', views.product_list, name='product_list_by_sort'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]