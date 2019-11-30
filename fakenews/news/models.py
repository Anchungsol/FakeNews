from django.conf import settings
from django.db import models
from django.utils import timezone


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
    pressName = models.CharField(max_length=50, primary_key=True)
    pressUrl = models.CharField(max_length=200)
    urlParameter = models.CharField(max_length=200)
    
class Users(models.Model):
    userId = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

class Record(models.Model):
    reIndex = models.IntegerField(primary_key=True)
    searchUrl = models.CharField(max_length=200)
    truth = models.BooleanField()
    newsDate = models.DateField()
    content = models.TextField()
    pressName = models.ForeignKey(Press, on_delete = models.CASCADE, db_column='pressName')
    userId = models.ForeignKey(Users, on_delete=models.SET_DEFAULT, default='Unknown', db_column='userId')
   


class FakeNews(models.Model):
    fnIndex = models.OneToOneField(Record, on_delete=models.CASCADE)
    fnGrammar = models.CharField(max_length=300)
    photoName = models.CharField(max_length=100)
    score = models.IntegerField()


class Grammar(models.Model):
    grammar = models.CharField(max_length=50, primary_key=True)
