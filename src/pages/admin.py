from django.contrib import admin
from pages.models import Products, Posts, ProdCategories, PostCategories


class ProdAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'id', 'name', 'time_create', 'photo', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'categories')
    list_display_links = ('id', 'name')


class PostAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'id', 'name', 'time_create', 'photo', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'categories')
    list_display_links = ('id', 'name')


class PrCatAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'time_create')
    list_filter = ('time_create',)
    list_display_links = ('id', 'name')


class PsCatAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'time_create')
    list_filter = ('time_create',)
    list_display_links = ('id', 'name')


admin.site.register(Products, ProdAdmin)
admin.site.register(Posts, PostAdmin)
admin.site.register(ProdCategories, PrCatAdmin)
admin.site.register(PostCategories, PsCatAdmin)