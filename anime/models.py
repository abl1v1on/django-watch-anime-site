from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

import cv2
import random


class Anime(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    alt_title = models.CharField(max_length=100, verbose_name='Альтернативное название')
    description = models.TextField(verbose_name='Описание')
    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='Тип')
    studio = models.ForeignKey('Studio', on_delete=models.CASCADE, verbose_name='Студия')
    date_aired = models.DateField(verbose_name='Дата выхода')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    genre = models.ManyToManyField('Genre', related_name='anime_genre', verbose_name='Жанр')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, 
                               verbose_name='Статус', related_name='anime_status')
    episodes_quantity = models.PositiveIntegerField(verbose_name='Количество эпизодов')
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
    series_file = models.FileField(upload_to='anime_series/%Y/%m', verbose_name='Серии')
    series_frame = models.ImageField(upload_to='anime_series/frames/%Y', verbose_name='Кадры', null=True, blank=True)

    class Meta:
        db_table = 'anime_series'
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    # ДОДЕЛАТЬ!!!
    # Сохраняем в series_frame рандомный кадр из видео
    def save(self, *args, **kwargs):
        if self.series_file:
            # Открываем видео
            video_capture = cv2.VideoCapture(self.series_file.path)
            # Считываем кадры
            total_frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
            # Выбираем рандомный кадр
            random_frame_number = random.randint(0, int(total_frames))
            # Устанавливаем позицию видео на рандомном кадре
            video_capture.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)
            # Считываем кадр
            ret, frame = video_capture.read()
            # Сохраняем кадр как изобраение
            self.series_frame = frame
            # Закрываем видео
            video_capture.release()
        super().save(*args, **kwargs)

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
    
    def get_absolute_url(self):
        return reverse('anime:anime_by_status', kwargs={'status_url': self.slug})
    


class Genre(models.Model):
    genre_name = models.CharField(max_length=50, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    class Meta:
        db_table = 'genre'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genre_name
    
    def get_absolute_url(self):
        return reverse('anime:anime_by_genre', kwargs={'genre_url': self.slug})
    

class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='comment_user')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='comment_anime')
    comment_text = models.CharField(max_length=2000, verbose_name='Текст комментария')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'