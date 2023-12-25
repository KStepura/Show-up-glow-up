from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

def news_home(request):
    news = Articles.objects.all
    return render(request, 'news/news_home.html', {'news': news})

class TrackerDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail_view.html'
    context_object_name = 'news'
