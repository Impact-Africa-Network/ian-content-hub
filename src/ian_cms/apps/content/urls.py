from django.urls import path
from .views import *


# from .views import HomeView, PackageView, GetTemplateView, DataPrivacyView, OnlineBUsinessView, Contact, register,view_cart, ProductDetailView

app_name = 'ian_cms.apps.content'

urlpatterns = [
    path('', Home.as_view(), name='home'),


    

]
