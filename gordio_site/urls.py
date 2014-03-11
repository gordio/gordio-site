from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url="/vcard/"), name="index"),
    url(r'^articles/', include('articles.urls', namespace="articles")),
    url(r'^contacts/', include('contacts.urls', namespace="contacts")),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^vcard/$', 'flatpage', {'url': '/vcard/'}, name="vcard"),
    url(r'^(?P<url>.*/)$', 'flatpage'),
)


# Apply media file for development
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
