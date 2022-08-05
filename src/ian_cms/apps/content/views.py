from unicodedata import category
from django.shortcuts import render
from django.views import View
from . models import ContentCategory, ContentType
from django.contrib.auth.decorators import login_required

from ian_account.models import User

# Create your views here.

# class Home(View):
#     def get(self, request):
#         return render(request, 'index.html', {})


def home(request):
    fireside_videos = ContentType.objects.all().filter(ContentCategory_id=1)
    ptow_videos = ContentType.objects.all().filter(ContentCategory_id=2)
    articles = ContentType.objects.all().filter(ContentCategory_id=3)

    print(fireside_videos)

    # featured_fireside = fireside_videos.objects.get(content_id=1)
    # featured_ptow_video = ptow_videos.objects.get(content_id=1)
    # featured_article = articles.objects.get(content_id=1)

    context = {
        'fireside_videos': fireside_videos,
        # 'ptow_videos': ptow_videos,
        # 'articles': articles
    }
    return render(request, "index.html", context)


# @login_required
def firesides(request):
    fireside_videos = ContentType.objects.all().filter(ContentCategory_id=1)
    
    context = {
        'fireside_videos': fireside_videos,
    }
    return render(request, "fireside-videos.html", context)

# @login_required
def ptow(request):
    ptow_videos = ContentType.objects.all().filter(ContentCategory_id=2)

    context = {
        'ptow_videos': ptow_videos
    }
    return render(request, 'ptow.html', context)

# @login_required
def articles(request):
    articles = ContentType.objects.all().filter(ContentCategory_id=3)

    context = {
        'articles': articles
    }
    return render(request, 'articles.html', context)        

        
