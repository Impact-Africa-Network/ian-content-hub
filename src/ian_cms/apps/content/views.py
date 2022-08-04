from django.shortcuts import render
from django.views import View


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'index.html', {})

class Firesides(View):
    def get(self, request):
        return render(request, 'fireside-videos.html', {})

class PTOW(View):
    def get(self, request):
        return render(request, 'ptow.html', {})

class Articles(View):
    def get(self, request):
        return render(request, 'articles.html', {})        

        
