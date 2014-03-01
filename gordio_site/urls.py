from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="vcard.html"), name="vcard"),

    url(r'^admin/', include(admin.site.urls)),
)


# Apply media file for development
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
