from django.db import models

# Create your models here.
class Post(models.Model):
  author = models.CharField(max_length = 200)
  topic = models.CharField(max_length = 200)
  content = models.TextField(max_length= 200000)
  url = models.URLField(max_length=200)
  likes = models.IntegerField(null=True)
  comments = models.IntegerField(null=True)

  def __str__(self):
    return self.author

class topic(models.Model):
  name = models.CharField(max_length=200)

class topics(models.Model):
  name = models.CharField(max_length=200)
  color = models.CharField(max_length=20)
