from django import template
from pages.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return ProdCategories.objects.all()