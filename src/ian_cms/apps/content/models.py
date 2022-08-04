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
    ContentCategory = models.ForeignKey(on_delete=models.DO_NOTHING)
    title = models.CharField
    