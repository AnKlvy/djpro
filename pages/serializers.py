from rest_framework import serializers

from .models import *


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('slug', 'name', 'price', )
