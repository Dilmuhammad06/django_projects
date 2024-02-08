from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True,unique=True)
    reads = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='computer_cat')
    lang = models.ManyToManyField('Language', blank=True, related_name='language_cat')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True,unique=True)

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True,unique=True)

    def __str__(self):
        return self.name

