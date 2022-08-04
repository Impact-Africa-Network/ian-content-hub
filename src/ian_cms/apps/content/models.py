from operator import mod
from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.

class ContentCategory(models.Model):
    category_id = models.IntegerField(primary_key=TRUE)
    category_name = models.CharField(max_length=20)
    category_id = models.CharField(max_length=20)


class ContentType(models.Model):
    ContentCategory = models.ForeignKey("ContentCategory", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=30)
    media_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    