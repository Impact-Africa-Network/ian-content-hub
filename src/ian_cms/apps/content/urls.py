from django.urls import path
from .views import *
from . views import home
from . import views

app_name = 'ian_cms.apps.content'

urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', views.home, name="home"),
    path('firesides', Firesides.as_view(), name='firesides'),
    path('ptow', PTOW.as_view(), name='ptow'),
    path('articles', Articles.as_view(), name='articles'),
]
