from django.shortcuts import render, get_object_or_404
from .models import *

news = Articles.objects.all()
context_post = {}

def news_el(request, post_slug):
    post = get_object_or_404(Articles, slug=post_slug)
    context_post['post'] = post
    return render(request, 'news/news_el.html', context=context_post)