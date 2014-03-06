from django.views.generic import ListView, DetailView
from .models import Article


class ArticlesListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 8


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
