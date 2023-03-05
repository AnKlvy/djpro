from django import template
from pages.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return ProdCategories.objects.all()

@register.inclusion_tag('pages/list_categories.html')
def show_categories():
    cats = ProdCategories.objects.all()
    return {"cats":cats}