from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class ProdCategories(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категории продукта"
        verbose_name_plural = "Категории продуктов"
        ordering = ['-name']

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="Продукты")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.BigIntegerField(verbose_name="Цена")
    description = models.TextField(max_length=700, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    categories = models.ManyToManyField(
        ProdCategories, related_name='categories',
        related_query_name='products', verbose_name="Категории")
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product', kwargs={'prod_slug': self.slug})

    def img(self):
        return self.photo.url

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-name']

    def __str__(self):
        return self.name


class PostCategories(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Категории поста"
        verbose_name_plural = "Категории постов"
        ordering = ['-name']

    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=255, verbose_name="Пост")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(max_length=700, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    categories = models.ManyToManyField(PostCategories, related_name='categories', verbose_name="Категории")

    def get_absolute_url(self):
        return reverse('addpost', kwargs={'post_slug': self.slug})

    # def addpost(self):
    #     return reverse('addpost')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['name']

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product} * {self.quantity}'