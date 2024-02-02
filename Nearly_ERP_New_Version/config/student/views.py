from django.shortcuts import render,get_object_or_404
from .models import Student,Category,GroupPost


categories = Category.objects.all()
groups = GroupPost.objects.all()

def index(request):
    students = Student.objects.all()
    data = {
        'title':'Student Management',
        'students':students,
        'page':'Dashboard',
        'categories':categories,
        'groups':groups
    }
    
    return render(request, 'student/index.html', context=data)

def show_post(request,post_slug):
    student = get_object_or_404(Student,slug = post_slug)
    data = {
        'title':'Manager of Students',
        'page':'Student Post',
        'students':student,
        'categories':categories,
        'groups':groups
    }
    return render(request,'student/show_post.html',data)

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











# Student.objects.count() #Counter
# Student.objects.filter(pk__gt=2).count() #Counter with filter
# from django.db.models import Count,Sum,Avg,Max,Min #importing
# Student.objects.aggregate(Min('pk')) #Min pk
# Student.objects.aggregate(age = Min('pk')) #Min pk in var
# Student.objects.filter(pk__gt=2).aggregate(res = Max('pk') - Min('pk')) #Max pk - Min pk
# w = Student.objects.values('name','is_active').get(pk=1) #Selecting only needed ones
# w = Student.objects.values('name','cat__name').get(pk=1) #With category
# w = Student.objects.aggregate(Avg('pk')) #Avg
# w = Student.objects.aggregate(Sum('pk')) #Sum