from django.views.generic import ListView, DetailView
from .models import Article
from datetime import datetime


class ArticlesListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 8

    def get_queryset(self):
        """
        Return Articles greater than pub_date
        """
        return Article.objects.filter(
            pub_date__lte=datetime.now()
        ).order_by('-pub_date')


class ArticlesTaggedView(ArticlesListView):
    def get_queryset(self):
        """
        Return Articles tagged 'tag' and greater than pub_date
        """
        return Article.objects.filter(
            tags__slug=self.kwargs.get('slug'), pub_date__lte=datetime.now()
        ).order_by('-pub_date')


class ArticleDetailView(DetailView):
    context_object_name = 'article'

    def get_queryset(self):
        """
        Return Articles greater than pub_date
        """
        return Article.objects.filter(
            pub_date__lte=datetime.now()
        ).order_by('-pub_date')
