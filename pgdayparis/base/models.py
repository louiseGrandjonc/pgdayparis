from django.db import models

from datetime import datetime


class News(models.Model):
	posttime = models.DateTimeField(null=False, blank=False, default=datetime.now)
	title = models.CharField(max_length=200, null=False, blank=False)
	content = models.TextField(null=False, blank=False, help_text='You can use markdown in this field. Be careful, you get no preview...')
	tweeted = models.BooleanField(null=False, blank=False, default=False, help_text='Has been posted to twitter')

	def __unicode__(self):
		return "%s: %s" % (self.posttime, self.title)

	class Meta:
		ordering = ('-posttime', )
		verbose_name_plural = 'News articles'
