from django.urls import path
from . import views

urlpatterns = [
    path('main/',views.main, name='main'),
    path('features/',views.features, name='features'),
    path('pricing/',views.pricing, name='pricing'),
]