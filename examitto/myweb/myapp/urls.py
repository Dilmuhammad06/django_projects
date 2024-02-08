from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('cat_show/<slug:cat_slug>/',views.show_category,name='category_show'),
    path('language_show/<slug:lang_slug>/',views.lang_show,name='language_show'),
    path('read_more/<slug:book_slug>',views.read_more,name='read_more')
]
