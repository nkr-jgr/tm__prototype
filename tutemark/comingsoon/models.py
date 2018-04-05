from django.db import models
import datetime
# Create your models here.

class Response(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    response_time = models.DateTimeField()

class Feedbacks(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()
    feedback_time = models.DateTimeField(default=datetime.datetime.now())
