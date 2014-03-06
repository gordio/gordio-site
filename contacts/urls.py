from django.conf.urls import patterns, include, url
from .views import ContactsView


urlpatterns = patterns('',
    url(r'^$', ContactsView.as_view(), name="home"),
)
