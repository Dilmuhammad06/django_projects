from django.shortcuts import render,redirect,get_object_or_404
from .models import Computers,Category
from .forms import ComputersForm,CategoryForm


def index(request):
    computer = Computers.objects.all()
    category = Category.objects.all()
    data = {
        'title':'Student Management',
        'computers':computer,
        'cat':category
    }
    
    return render(request, 'student/index.html', context=data)

def add_product(request):
    if request.method == 'POST':
        form = ComputersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ComputersForm()

    data = {
        'title': 'Add Computer',
        'form': form,
    }
    return render(request, 'student/add_product.html', data)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()

    data = {
        'title': 'Add Category',
        'form': form,
    }
    return render(request, 'student/add_category.html', data)

def prods(request, cat_slug):
    slug = get_object_or_404(Category, slug=cat_slug)
    category = Category.objects.all()
    computers = Computers.objects.filter(cat=slug)

    data = {
        'title': 'Products',
        'cat': category,
        'comp': computers,
        'slug':slug
    }

    return render(request, 'student/prod_view.html', data)