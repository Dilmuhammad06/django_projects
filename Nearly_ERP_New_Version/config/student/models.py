from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    cat = models.ForeignKey('Category',on_delete = models.PROTECT, related_name='students')
    group = models.ManyToManyField('GroupPost',blank=True,related_name='group_student')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.name

class GroupPost(models.Model):
    group_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.group_name