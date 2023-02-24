from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news/', views.news_page, name='news'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
] 
 