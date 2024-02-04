from django.contrib import admin
from .models import Computers,Category

admin.site.register([Computers,Category])