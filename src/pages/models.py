from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
	owner = models.IntegerField()
	text = models.CharField(max_length=150)

#class Note(models.Model):
#	owner = models.ForeignKey(User, on_delete=models.CASCADE)
#	text = models.CharField(max_length=150)