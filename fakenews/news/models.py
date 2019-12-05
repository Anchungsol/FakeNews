from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Press(models.Model):
    pressId = models.AutoField(primary_key=True)
    pressName = models.CharField(max_length=50)
    pressUrl = models.CharField(max_length=200)

class Users(models.Model):
    userId = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

class Record(models.Model):
    reIndex = models.AutoField(primary_key=True)
    searchUrl = models.CharField(max_length=200)
    truth = models.BooleanField()
    newsDate = models.CharField(max_length=20)
    content = models.TextField()

class FakeNews(models.Model):
    grammarCount = models.IntegerField()
    urlError = models.CharField(max_length=200)
    photoError = models.CharField(max_length=100)
    dateError = models.CharField(max_length=100)
    score = models.IntegerField()

class Grammar(models.Model):
    grammar = models.CharField(max_length=50, primary_key=True)
