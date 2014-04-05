from django.conf.urls import patterns, include, url
from .views import ArticlesListView, ArticleDetailView, ArticlesTaggedView
from .feeds import ArticlesFeed


urlpatterns = patterns('',
    url(r'^$', ArticlesListView.as_view(), name="list"),
    url(r'^tagged/(?P<slug>.*)$', ArticlesTaggedView.as_view(), name="tagged"),
    url(r'^view/(?P<slug>.*)$', ArticleDetailView.as_view(), name="view"),
    url(r'^feed/$', ArticlesFeed(), name="feed"),
)
