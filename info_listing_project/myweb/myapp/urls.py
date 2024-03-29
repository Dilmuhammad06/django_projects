from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('info/<int:id>/', views.info, name='info'),
]