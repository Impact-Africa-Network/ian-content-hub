from django.contrib import admin
from . models import ContentCategory, ContentType
# Register your models here.

admin.site.register(ContentCategory)
admin.site.register(ContentType)