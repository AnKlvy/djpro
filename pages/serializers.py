from rest_framework import serializers

from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)

    class Meta:
        model = Products
        fields = "__all__"
