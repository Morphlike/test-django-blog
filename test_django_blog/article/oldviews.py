from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CommentArticleForm

from hexlet_django_blog.article.models import Article

class IndexView(View):
 
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:5]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })
    

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })
    

class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'comment.html', {'form': form}) # Передаем нашу форму в контексте