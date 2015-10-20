from django.db import models


class Event(models.Model):
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.event_text

class Choice(models.Model):
    event = models.ForeignKey(Event)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
	return self.votes
