from django.shortcuts import render, get_object_or_404
from .models import Article
from django.utils.translation import gettext as _


# Create your views here.

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})


def single_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'single_article.html', {'article': article,})
