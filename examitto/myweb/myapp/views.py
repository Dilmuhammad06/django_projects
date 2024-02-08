from django.shortcuts import render,get_object_or_404
from .models import Books,Category,Language




def index(request):
    books = Books.objects.order_by('name')
    category = Category.objects.all()
    language = Language.objects.all()

    data={
    'books':books,
    'cat':category,
    'lang':language
}    
    return render(request,'index.html',data)

def show_category(request,cat_slug):

    slug = get_object_or_404(Category,slug=cat_slug)
    book = Books.objects.filter(cat=slug)

    data={
    'books':book
}    
    return render(request,'category_show.html',data)

def lang_show(request,lang_slug):

    slug = get_object_or_404(Language,slug = lang_slug)
    books = Books.objects.filter(lang=slug)

    data={
    'books':books
}    
    return render(request,'lang_show.html',data)

def read_more(request,book_slug):

    book = get_object_or_404(Books,slug = book_slug)

    data={
        'book':book
    }
    return render(request,'read_more.html',data)