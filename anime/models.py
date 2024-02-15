from django.db import models
from django.urls import reverse


class Anime(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    alt_title = models.CharField(max_length=100, verbose_name='Альтернативное название')
    description = models.TextField(verbose_name='Описание')
    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='Тип')
    studio = models.ForeignKey('Studio', on_delete=models.CASCADE, verbose_name='Студия')
    date_aired = models.DateField(verbose_name='Дата выхода')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    genre = models.ManyToManyField('Genre', related_name='anime_genre', verbose_name='Жанр')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name='Статус')
    duration = models.CharField(max_length=50, verbose_name='Продолжительность')
    quality = models.CharField(max_length=50, verbose_name='Качество')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    cover = models.ImageField(upload_to='anime_covers/%Y/%m', 
                              verbose_name='Обложка', null=True, blank=True)
    
    class Meta:
        db_table = 'anime'
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime:anime_detail', kwargs={'slug': self.slug})
    

class AnimeSeries(models.Model):
    anime_id = models.ForeignKey('Anime', related_name='anime_series', on_delete=models.CASCADE, verbose_name='Аниме')
    series_file = models.FileField(upload_to='anime_series/%Y/%m', verbose_name='Серии', null=True, blank=True)

    class Meta:
        db_table = 'anime_series'
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    def __str__(self):
        return self.series_file.url
    

class Type(models.Model):
    type_name = models.CharField(max_length=50, verbose_name='Тип')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.type_name
    

class Studio(models.Model):
    studio_name = models.CharField(max_length=50, verbose_name='Студия')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    class Meta:
        db_table = 'studio'
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'

    def __str__(self):
        return self.studio_name
    

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    class Meta:
        db_table = 'catrgory'
        verbose_name = 'Катеогия'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Status(models.Model):
    status_name = models.CharField(max_length=50, verbose_name='Статус')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.status_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=50, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    class Meta:
        db_table = 'genre'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genre_name
