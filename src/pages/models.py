from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Note(models.Model):
	user_id = models.IntegerField()
	text = models.CharField(max_length=150)

class Log(models.Model):
    user_id = models.IntegerField()
    action = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

#class Note(models.Model):
#	owner = models.ForeignKey(User, on_delete=models.CASCADE)
#	text = models.CharField(max_length=150)