from django.contrib import admin
from .models import ContentCategory, ContentType


admin.site.register(ContentCategory)
admin.site.register(ContentType)