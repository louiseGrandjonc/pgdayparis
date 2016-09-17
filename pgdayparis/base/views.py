# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import TemplateDoesNotExist, loader, Context
from django.template import RequestContext
from django.conf import settings

import random
import simplejson as json
import markdown
from datetime import datetime

from pgdayparis.base.models import *

# from templateextra import context_template_additions


def get_year(host):
    current_year = settings.DEFAULT_YEAR
    for year in settings.PGDAY_YEARS:
        if host.startswith(str(year)):
            current_year = year
    return current_year

class PgConfContext(RequestContext):
    def __init__(self, request, year=None):
        RequestContext.__init__(self, request)
        if not year:
            year = settings.DEFAULT_YEAR
        self.update({
            'linkbase': '/%d/' % year,
            'mediabase': '/',
            'year': year
        })
        # self.update(context_template_additions())

# URLs to redirect to dynamic pages
def get_redirects(year):
    return {
    'commitee':     '/%d/qui-sommes-nous/' % year,
    'committee':    '/%d/qui-sommes-nous/' % year,
    'feedback':     'https://www.postgresql.eu/events/feedback/pgdayparis/%d' % year,
    'm':            'https://www.postgresql.eu/m/pgdayparis%d/' % year,
    'programme':    'http://www.postgresql.eu/events/schedule/pgdayparis%d/' % year,
    'registration': '/%d/inscriptions/' % year,
    'schedule':     'http://www.postgresql.eu/events/schedule/pgdayparis%d/' % year,
    'sessions':     'http://www.postgresql.eu/events/sessions/pgdayparis%d/' % year,
}


def index(request, year):
    if year:
        try:
            year = int(year)
            if year not in settings.PGDAY_YEARS:
                year = None
        except:
            pass

    host = request.META.get('HTTP_HOST')
    year = get_year(host) if not year else year
    context = PgConfContext(request, year=year)
    template_name = 'pgdayparis%d/pages/index.html' % year
    return render_to_response(template_name,
                              {},
                              context)


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
    splits = url.split('/')
    year = None

    
    if len(splits) > 1:
        try:
            year = int(splits[0])
            url = splits[1]
            if year not in settings.PGDAY_YEARS:
                year = None
        except:
            pass
    host = request.META.get('HTTP_HOST')
    year = get_year(host) if not year else year
    context = PgConfContext(request, year=year)
    redirects = get_redirects(year)
    try:
        # Some sanity
        if url.find('..') > -1:
            raise TemplateDoesNotExist

        # Some URLs are redirects
        if redirects.has_key(url):
            return HttpResponseRedirect(redirects[url])

        t = loader.get_template('pgdayparis%d/pages/%s.html' % (year, url))
        return HttpResponse(t.render(context))
    except TemplateDoesNotExist, e:
        raise Http404('Page not found')
