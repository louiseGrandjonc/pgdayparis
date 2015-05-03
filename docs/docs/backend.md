# Backend of your website

There you are! You'll find a few things about the backend of your pg event website.

We won't discuss here the backend of pgeu. Don't worry about it, it works damn well !

Let's take a really simple example. Let's say that for your website you want :

- A news page (with a database containing news objects)
- A few static pages (home page, presentation of your call for papers, how to get to the event, the sponsors, etc.)
- The pgeu pages (registrations, schedule, etc.)

## Page with a django view

## Sending back static pages

If you are as lazy as us, adding for each static page an url in the urls.py and a view that basicaly just render the template is annoying. For this matter, here is a piece of code to handle all static pages the same way.


In your urls.py you can add :
```
urlpatterns = patterns(
...
(r'^(.*)/$', 'myevent.views.static_fallback'),
)
```

And in the views.py you can add :

```
def static_fallback(request, url):
    try:
        # Some sanity
        if url.find('..') > -1:
           raise TemplateDoesNotExist
        t = loader.get_template('pgdayparis2015/pages/%s.html' % url)
        return HttpResponse(t.render(PgConfContext(request)))
    except TemplateDoesNotExist, e:
           raise Http404('Page not found')
```

PgConfContext is the context that you personnalized. The PgConfContext should contain at least two things :
- linkbase
- mediabase

This is really usefull to build the urls that are in common with pgeu pages (for instance the menu urls). But we'll explain that more precisely in the frontend part !

## pgeu pages

You don't actually need to do anything in the backend to allow your website to communicate with pgeu's website. Of course, as said previously you need to have a specific context that is really useful. There is an example of this context :

```
class PgConfContext(RequestContext):
      def __init__(self, request):
          RequestContext.__init__(self, request)
          self.update({'linkbase': '/', 'mediabase': '/'})
```

We strongly invite you to read the frontend part to understand how your template should be organized !
