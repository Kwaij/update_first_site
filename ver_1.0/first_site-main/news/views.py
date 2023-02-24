from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDV(DetailView):
    model = Articles
    template_name = 'news/news_dv.html'
    context_object_name = 'article'
