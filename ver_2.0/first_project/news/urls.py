from django.urls import path
from . import views

urlpatterns = [
    path('<slug:post_slug>/', views.news_el, name='news_el')
]
