from django import template
from tech.models import *
from news.models import *
from menu.models import *

register = template.Library()

@register.simple_tag()
def get_tech_categories():
    return Tech.objects.all()

@register.simple_tag()
def get_articles_categories():
    return Articles.objects.all()

@register.simple_tag()
def get_menu_categories():
    return Menu.objects.all()

@register.inclusion_tag('main/menu.html')
def show_menu():
    menu = Menu.objects.all()
    return {'menu': menu}