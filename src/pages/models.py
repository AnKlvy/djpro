from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    description = models.TextField(max_length=700)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProdCategories(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Products, related_name='categories')

    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=700)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PostCategories(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Posts, related_name='categories')

    def __str__(self):
        return self.name
