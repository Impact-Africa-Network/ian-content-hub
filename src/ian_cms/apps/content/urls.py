from django.urls import path
from .views import *

app_name = 'ian_cms.apps.content'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('firesides', Firesides.as_view(), name='firesides'),
    path('ptow', PTOW.as_view(), name='ptow'),
    path('articles', Articles.as_view(), name='articles'),





    

]
