from django.db import models

class Article(models.Model):

    header_img = models.ImageField()
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=70)
    body = models.TextField()
    timestamp = models.DateField(auto_now=True)