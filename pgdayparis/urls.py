from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from base.feeds import NewsFeed

urlpatterns = patterns('',
	(r'^$', 'base.views.index'),

    (r'^news.rss$', NewsFeed()),
    (r'^news.json$', 'base.views.newsjson'),

    # This will never happen in production, handled by webserver
	(r'^files/(.*)$', 'django.views.static.serve', {
			'document_root': '../files',
	}),
    (r'^(favicon.ico)$', 'django.views.static.serve', {
			'document_root': '../files/img',
	}),

    # Admin for some models
	(r'^admin/', include(admin.site.urls)),

    # Static pages for everything else
    (r'^(.*)/$', 'base.views.static_fallback'),
)
