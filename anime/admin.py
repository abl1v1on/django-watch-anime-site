from django.contrib import admin

from . import models


class AnimeSeriesInlime(admin.TabularInline):
    model = models.AnimeSeries


@admin.register(models.Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title', 'alt_title', 'type', 'studio', 'category', 'status', 'views']
    list_display_links = ['title', ]
    search_fields = ['title', ]
    inlines = [AnimeSeriesInlime, ]
    filter_horizontal = ('genre', )
    prepopulated_fields = {'slug': ('title', )}


@admin.register(models.AnimeSeries)
class AnimeSeriesAdmin(admin.ModelAdmin):
    list_display = ['anime_id', 'series_file']
    list_display_links = ['anime_id', ]


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'slug']
    list_display_links = ['type_name', ]


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['studio_name', 'slug']
    list_display_links = ['studio_name', ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    list_display_links = ['category_name', ]


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['status_name', 'slug']
    list_display_links = ['status_name', ]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'slug']
    list_display_links = ['genre_name', ]   


@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'anime', 'comment_text', 'date_create']
    list_display_links = ['user', ]