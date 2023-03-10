# Generated by Django 4.1.5 on 2023-03-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Категории поста',
                'verbose_name_plural': 'Категории постов',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='ProdCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Категории продукта',
                'verbose_name_plural': 'Категории продуктов',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Продукты')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.BigIntegerField(verbose_name='Цена')),
                ('description', models.TextField(max_length=700, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('categories', models.ManyToManyField(related_name='categories', to='pages.prodcategories',
                                                      verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='Пост')),
                ('description', models.TextField(max_length=700, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('categories', models.ManyToManyField(related_name='categories', to='pages.postcategories',
                                                      verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['name'],
            },
        ),
    ]