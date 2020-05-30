from django.shortcuts import render
from .models import Article

# Create your views here.

def index(requests):

    article_list = Article.objects.all()
    ordered_article_list = article_list[::-1]

    return render(requests, 'articles.html', {"articles":ordered_article_list}) 