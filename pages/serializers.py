from rest_framework import serializers

from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Products
        fields = "__all__"
