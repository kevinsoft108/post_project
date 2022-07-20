from django.db import models

# Create your models here.
class Post(models.Model):
  author = models.CharField(max_length = 200)
  # topic = models.CharField(max_length = 200)
  content = models.TextField(max_length= 200000)
  image = models.ImageField(upload_to='images/', blank=True, null=True)
  url = models.URLField(max_length=200, null=True)
  likes = models.IntegerField(null=True)
  comments = models.IntegerField(null=True)
  topic = models.ForeignKey('Topics', on_delete=models.CASCADE)


  def __str__(self):
    return self.author

class topic(models.Model):
  name = models.CharField(max_length=200)

class Topics(models.Model):
  name = models.CharField(max_length=200)
  color = models.CharField(max_length=20)
