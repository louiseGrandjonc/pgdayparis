#!/usr/bin/env python
#
# Tool to post newly posted news to twitter
#
# We run this in cron and poll the database, because, well, it's easier
# that way...
#

import os
import sys
import ConfigParser

# Set up to run in django env
from django.core.management import setup_environ
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), '../pgdayparis'))
import settings
setup_environ(settings)


from twitterclient import TwitterClient

from pgdayparis.base.models import News

cfg = ConfigParser.ConfigParser()
cfg.read('twitter.ini')

if __name__=="__main__":
	twitter = TwitterClient(cfg)

	for article in News.objects.filter(tweeted=False):
		# Tweet this article
		print "Tweeting: %s" % article

		msg = "Update: %s - http://www.pgday.paris/" % article.title

		ret_dict = twitter.twitter_request('statuses/update.json', 'POST', {
			'status': msg.encode('utf-8'),
			})

		if not ret_dict.has_key('created_at'):
			# Something went wrong!
			if ret_dict.has_key('error'):
				print "Failed to tweet: %s" % ret_dict['error']
			elif ret_dict.has_key('errors'):
				print "Failed to tweet: %s" % " :: ".join([r['message'] for r in ret_dict['errors']])
			else:
				print "Unparseable response from twitter: %s!" % ret_dict
			print "Going to flag this as posted anyway, so we don't repost!"

		# Now flag it as tweeted. Django default will immediately commit
		# our transaction.
		article.tweeted=True
		article.save()

