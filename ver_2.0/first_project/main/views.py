from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

from tech.models import *
from news.models import *

tech = Tech.objects.all()
news = Articles.objects.all()
context_list = {}

class TechPage(ListView):
    model = Tech
    template_name = 'main/index.html'
    context_object_name = 'page_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def index(request):
    paginator = Paginator(tech, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context_list['page_obj'] = page_obj
    return render(request, 'main/index.html', context=context_list)

class NewsPage(ListView):
    model = Articles
    template_name = 'main/news.html'
    context_object_name = 'page_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def news_page(request):
    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context_list['page_obj'] = page_obj
    return render(request, 'main/news.html', context=context_list)

def about(request):
    return render(request, 'main/about.html', context=context_list)

def login(request):
    return render(request, 'main/login.html', context=context_list)    