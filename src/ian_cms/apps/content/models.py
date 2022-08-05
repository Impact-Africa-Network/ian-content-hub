from operator import mod
from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.
FIRESIDE = 'fireside'
PTOW = 'ptow'
ARTICLES = 'articles'

CATEGORY_NAMES = [
    (FIRESIDE, "fireside"),
    (PTOW, "ptow"),
    (ARTICLES, "articles")
]

class ContentCategory(models.Model):
    category_id = models.IntegerField(primary_key=TRUE)
    category_name = models.CharField(max_length=20, choices=CATEGORY_NAMES)

    def __str__(self):
        return self.category_name


class ContentType(models.Model):
    ContentCategory = models.ForeignKey("ContentCategory", on_delete=models.DO_NOTHING)
    content_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=30)
    media_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ()
    