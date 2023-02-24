from django.shortcuts import render
from .models import Tech
from django.views.generic import DetailView

def index(request):
    tech = Tech.objects.all()
    return render(request, 'main/index.html', {'tech': tech})

def about(request):
    return render(request, 'main/about.html')

class TechDV(DetailView):
    model = Tech
    template_name = 'main/tech_dv.html'
    context_object_name = 'tech'

