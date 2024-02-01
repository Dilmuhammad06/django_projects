from django.shortcuts import render,get_object_or_404
from .models import Student,Category,GroupPost

# Create your views here.

categories = Category.objects.all()
groups = GroupPost.objects.all()

def index(request):
    student = Student.objects.all()
    data = {
        'title':'Student Management',
        'students':student,
        'page':'Dashboard',
        'categories':categories,
        'groups':groups
    }
    
    return render(request, 'student/index.html', context=data)

def show_post(request,post_slug):
    student = get_object_or_404(Student,slug=post_slug)
    data = {
        'title':'Student Management',
        'page':'Student Post',
        'students':student,
        'categories':categories,
        'groups':groups
    }
    return render(request,'student/post.html',data)

def show_cat(request,cat_slug):
    category = get_object_or_404(Category,slug=cat_slug)
    students = category.students.filter(is_active=True)
    data = {
        'title':'Student Management',
        'page':f'student{category.name}',
        'students':students,
        'categories':categories,
        'groups':groups
    }

    return render(request, 'student/index.html', context=data)

def show_group(request,group_slug):
    group = get_object_or_404(GroupPost,group_slug)
    students = group.group_student.filter(is_active=True)

    data = {
        'title':'Student Management',
        'page':f'student{group.group_name}',
        'students':students,
        'categories':categories,
        'groups':groups
    }

    return render(request, 'student/index.html', context=data)
