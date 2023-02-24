from django.urls import path
from . import views

urlpatterns = [
    path('<slug:post_slug>/', views.tech_el, name='tech_el')
] 
 