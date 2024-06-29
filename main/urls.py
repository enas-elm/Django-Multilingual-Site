# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'), # Default URL redirect to all articles
    path('articles/', views.articles, name='articles'), # URL for all articles
    path('single_article/<int:article_id>/', views.single_article, name='single_article') # URL for a single article
]
