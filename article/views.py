from django.shortcuts import render
from blog_app.models import Article

def article_by_id(requests, article_id):
    article = Article.objects.get(id=article_id)

    return render(requests, 'view.html', {'article':article})