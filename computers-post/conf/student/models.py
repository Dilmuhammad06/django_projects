from django.db import models

class Computers(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='computer_cat')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.name