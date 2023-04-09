from django.contrib import admin
from django.utils.safestring import mark_safe

from pages.models import Products, Posts, ProdCategories, PostCategories


class ProdAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'id', 'name', 'time_create', 'get_html_photo', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'categories')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        'name', 'slug', 'categories', 'description', 'photo', 'get_html_photo', 'is_published', 'time_create',
        'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class PostAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'id', 'name', 'time_create', 'get_html_photo', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'categories')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        'name', 'slug', 'categories', 'description', 'photo', 'get_html_photo', 'is_published', 'time_create',
        'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class PrCatAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'time_create')
    list_filter = ('time_create',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


class PsCatAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'time_create')
    list_filter = ('time_create',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Products, ProdAdmin)
admin.site.register(Posts, PostAdmin)
admin.site.register(ProdCategories, PrCatAdmin)
admin.site.register(PostCategories, PsCatAdmin)

admin.site.site_title = 'Админ-панель лучшего программиста'
admin.site.site_header = 'Админ-панель лучшего программиста'
