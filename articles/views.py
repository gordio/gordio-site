from django.views.generic import ListView, DetailView
from .models import Article
from datetime import datetime


class ArticlesListView(ListView):
    context_object_name = 'articles'
    paginate_by = 8

    def get_queryset(self):
        """
        Return Articles greater than pub_date
        """
        return Article.objects.filter(
            pub_date__lte=datetime.now()
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
