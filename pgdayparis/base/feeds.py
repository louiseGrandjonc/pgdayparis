from django.contrib.syndication.views import Feed

from pgdayparis.base.models import News

from datetime import datetime, time

class NewsFeed(Feed):
	title = description = "pgday.paris 2015 News"
	link = "http://pgday.paris/"

	description_template = 'pgdayparis/rss/news_description.html'
	title_template = 'pgdayparis/rss/news_title.html'

	def items(self):
		return News.objects.all().order_by('-posttime')[:5]

	def item_link(self, obj):
		# Don't bother with individual links, just send the user always
		# to the frontpage.
		return "http://pgday.paris/"

	def item_pubdate(self, obj):
		return obj.posttime
