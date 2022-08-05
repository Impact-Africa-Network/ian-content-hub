from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from ian_account.models import User

# Create your views here.

# class Home(View):
#     def get(self, request):
#         return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

# @login_required
def firesides(request):
    return render(request, 'fireside-videos.html', {})

# @login_required
def ptow(self, request):
    return render(request, 'ptow.html', {})

# @login_required
def articles(self, request):
    return render(request, 'articles.html', {})        

        
