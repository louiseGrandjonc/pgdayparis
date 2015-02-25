from django.conf.urls import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

from pgdayparis.base.feeds import NewsFeed

urlpatterns = patterns(
    '',
    (r'^$', 'pgdayparis.base.views.index'),
    (r'^news.rss$', NewsFeed()),
    (r'^news.json$', 'pgdayparis.base.views.newsjson'),

    # Admin for some models
    (r'^admin/', include(admin.site.urls)),

    # Static pages for everything else
    (r'^(.*)/$', 'pgdayparis.base.views.static_fallback'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
