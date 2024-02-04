from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_prod/',views.add_product,name='add_product'),
    path('add_cat/',views.add_category,name='add_category'),
    path('prods/<slug:cat_slug>/',views.prods,name='prods')


]
