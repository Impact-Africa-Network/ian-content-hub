from django.urls import path
from .views import *
from . import views

app_name = 'ian_cms.apps.content'

urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', views.home, name='home'),
    path('firesides', views.firesides, name='firesides'),
    path('ptow', views.ptow, name='ptow'),
    path('articles', views.articles, name='articles'),  
]
