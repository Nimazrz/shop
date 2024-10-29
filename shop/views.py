from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def  product_list(request, category_slug=None, sort_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
         category = get_object_or_404(Category, slug=category_slug)
         products = products.filter(category=category)

    sorts = Sort.objects.all()
    if sort_slug:
        sort = get_object_or_404(Sort, slug=sort_slug)
        products = products.order_by(f'{sort.slug}')
    context = {
        'category': category,
        'categories':categories,
        'products': products,
        'sorts': sorts,
    }
    return render(request, 'shop/list.html', context)

def  product_list(request, category_slug=None, sort_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
         category = get_object_or_404(Category, slug=category_slug)
         products = products.filter(category=category)

    sorts = Sort.objects.all()
    if sort_slug:
        sort = get_object_or_404(Sort, slug=sort_slug)
        products = products.order_by(f'{sort.slug}')
    context = {
        'category': category,
        'categories':categories,
        'products': products,
        'sorts': sorts,
    }
    return render(request, 'shop/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    context ={
        'product': product,
    }
    return render(request, 'shop/detail.html', context)