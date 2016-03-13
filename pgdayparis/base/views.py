# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import TemplateDoesNotExist, loader, Context
from django.template import RequestContext

import random
import simplejson as json
import markdown
from datetime import datetime

from pgdayparis.base.models import *

# from templateextra import context_template_additions


class PgConfContext(RequestContext):
    def __init__(self, request):
        RequestContext.__init__(self, request)

        self.update({'linkbase': '/', 'mediabase': '/'})
        # self.update(context_template_additions())

# URLs to redirect to dynamic pages
redirects = {
    'commitee':     '/qui-sommes-nous/',
    'committee':    '/qui-sommes-nous/',
    'contact':      '/qui-sommes-nous/',
    'feedback':     'https://www.postgresql.eu/events/feedback/pgdayparis2016/',
    'm':            'https://www.postgresql.eu/m/pgdayparis2016/',
    'programme':    'http://www.postgresql.eu/events/schedule/pgdayparis2016/',
    'registration': '/inscriptions/',
    'schedule':     'http://www.postgresql.eu/events/schedule/pgdayparis2016/',
    'sessions':     'http://www.postgresql.eu/events/sessions/pgdayparis2016/',
    'venue':        '/comment-venir/',
}


def index(request):
    posts = News.objects.all().order_by('-posttime')[:4]

    # random.shuffle(frontimages)

    return render_to_response('pgdayparis2016/pages/index.html', {
        'posts': posts,
        # 'slides': frontimages,
    }, PgConfContext(request))


def newsjson(request):
    since = request.GET.get('since', None)
    if since:
        d = datetime.fromtimestamp(float(since)/1000)
        news = News.objects.filter(posttime__gt=d).order_by('-posttime')
    else:
        news = News.objects.all().order_by('-posttime')
    resp = HttpResponse(mimetype='application/json')
    resp.write('news_jsonp(')
    json.dump([{'d': n.posttime.isoformat(), 't': n.title, 'c': markdown.markdown(n.content, safe_mode=True)} for n in news], resp)  # noqa
    resp.write(')')
    return resp


def static_fallback(request, url):
    try:
        # Some sanity
        if url.find('..') > -1:
            raise TemplateDoesNotExist

        # Some URLs are redirects
        if redirects.has_key(url):
            return HttpResponseRedirect(redirects[url])

        t = loader.get_template('pgdayparis2016/pages/%s.html' % url)
        return HttpResponse(t.render(PgConfContext(request)))
    except TemplateDoesNotExist, e:
        raise Http404('Page not found')
