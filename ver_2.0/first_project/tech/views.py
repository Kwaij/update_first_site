from django.shortcuts import render, get_object_or_404
from .models import *

tech = Tech.objects.all()
context_post = {}

def tech_el(request, post_slug):
    post = get_object_or_404(Tech, slug=post_slug)
    context_post['post'] = post
    return render(request, 'tech/tech_el.html', context=context_post)
