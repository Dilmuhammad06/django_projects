from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show/<slug:post_slug>/',views.show_post, name='student_post'),
    path('cat/<slug:cat_slug>/',views.show_cat,name='cat'),
    path('group/<slug:group_slug>/',views.show_group,name='group')
]
