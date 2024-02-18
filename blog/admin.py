from django.contrib import admin

from .models import Blog, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_create', 'user')
    filter_horizontal = ('tags', )
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug')
    