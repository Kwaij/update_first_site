from django.views.generic import ListView
from django.db.models import Q
from itertools import chain

from tech.models import *
from news.models import *

tech = Tech.objects.all()
news = Articles.objects.all()

class Search(ListView):
    template_name = 'search/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q') 
        
        if query: 
            tech_query = Tech.objects.filter(Q(title__icontains = query) | Q(full_text__icontains = query))
            articles_query = Articles.objects.filter(Q(title__icontains = query) | Q(full_text__icontains = query))
            results = chain(tech_query, articles_query)
        else:
            results = None
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
