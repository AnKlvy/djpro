from django.core.cache import cache
from django.db.models import Count

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'addpost'},
        {'title': "Contact us", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        print("DataMixin kwargs=", kwargs)
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = ProdCategories.objects.annotate(Count('products'))
            print('DataMixin cats from if not cats=', cats)
            cache.set('cats', cats, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
