import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
	title = models.CharField(max_length=50)
	text = models.CharField(max_length=4000)
	pub_date = models.DateTimeField()
	upd_date = models.DateTimeField()
	up_votes = models.IntegerField(default=0)
	down_votes = models.IntegerField(default=0)
	reference = models.CharField(max_length=200)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return self.title