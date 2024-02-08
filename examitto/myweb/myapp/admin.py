from django.contrib import admin
from .models import Books,Category,Language

admin.site.register([Books,Category,Language])