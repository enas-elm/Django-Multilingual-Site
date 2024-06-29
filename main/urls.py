# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('articles/', views.articles, name='articles'),
    path('single_article/<int:article_id>/', views.single_article, name='single_article')
]
