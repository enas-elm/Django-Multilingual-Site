# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('articles_list/', views.articles_list, name='articles_list'),
    path('single_article/<int:article_id>/', views.single_article, name='single_article')
]
