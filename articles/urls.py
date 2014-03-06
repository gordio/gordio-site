from django.conf.urls import patterns, include, url
from .views import ArticlesListView, ArticleDetailView


urlpatterns = patterns('',
    url(r'^$', ArticlesListView.as_view(), name="list"),
    url(r'^view/(?P<slug>.*)$', ArticleDetailView.as_view(), name="view"),
)
