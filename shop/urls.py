from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shop'
urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('products/sort/<slug:sort_slug>', views.product_list, name='product_list_by_sort'),
    path('products/<slug:category_slug>/sort/<slug:sort_slug>', views.product_list, name='product_list_by_sort'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.loged_out, name='logout'),
    path('register', views.register, name='register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url='done'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password-reset/', auth_views.PasswordResetView.as_view(success_url='done'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(success_url='/password-reset/complete'),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]