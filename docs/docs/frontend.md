# Frontend of your website

It's where the magic happens ! Okay, so you know basically how django templates work (otherwise, [read there doc](https://docs.djangoproject.com/en/1.8/intro/tutorial01/), it's amazing)

To communicate with pgeu you need :

- A single css file that will be reused by pgeu to keep consistancy between your pages and there pages
- A base-myevent.html that will be used by pgeu and their code will be included in it.

## The base-myevent.html template

This is completly essential ! It's this template that pgeu will use to include their code. So let's take a moment to explain how it works, and the best way is with and example right ?

```
{% extends "myevent/base.html" %}
{% block myeventcontent %}
  <section class="like-you">
    <article id="pgeubase" class="col-md-12 content left-col right-col">
      {% block content %}{% endblock %}
    </article>
  </section>
{% endblock %}
```

First you have your base.html. It should contain the common things to all your pages. So you should find there your menu, you should include your css and your javascript files if you have some. We'll precise a few things concerning the links in the next part.

Here the <section> and <article> are there for the design with the css. What is important is that you have two blocks. In the block content will be included all the code from the pgeu templates.

## Menu, media and staticfiles links

Usually, we, django developpers 
