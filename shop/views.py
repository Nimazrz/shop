from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,Http404
from .forms import *

# Create your views here.

def product_list(request, category_slug=None, sort_slug=None):
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

    # pagination{
    paginator = Paginator(products, 10)  # Show 2 products per page
    page_number = request.GET.get('page', 1)
    try:
        products = paginator.get_page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # }
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


def loged_out(request):
    logout(request)
    return render(request,'registration/logged_out.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/register_done.html', {'user':user})
    else:
        form=UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})
