from django.shortcuts import render, redirect
from . import forms
from .models import *

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    #Собираем названия всех продуктов
    product_info = Product.objects.all()
    #Собираем названия всех категорий
    category_info = Category.objects.all()

    # Передаем данные на фронт
    context = {
        'form': search_bar,
        'product': product_info,
        'category': category_info
    }

    return render(request, 'index.html', context)


def product_page(request, pk):
    product_info = Product.objects.get(id=pk)

    #Передаем данные на фронт
    context = {'product': product_info}
    return render(request, 'about_product.html', context)

def category_page(request, pk):
    category_info = Category.objects.get(id=pk)
    product_info = Product.objects.filter(product_category=category_info)

    #Передаем данные на фронт
    context = {'products': product_info}

    return render(request, 'about_category.html', context)

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = Product.objects.get(product_name__icontains=get_product)
            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')


def about_page(request):
    return render(request, 'about.html')
def contact_page(request):
    return render(request, 'contacts.html')
