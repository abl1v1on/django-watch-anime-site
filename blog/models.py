from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Звголовок')
    content = CKEditor5Field(verbose_name='Контент', config_name='extends')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    date_create = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='blog_tags', verbose_name='Теги')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    cover = models.ImageField(upload_to='post_cover/', verbose_name='Изображение')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'post_url': self.slug})
    


class Tag(models.Model):
    tag_name = models.CharField(max_length=60, verbose_name='Название тега')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    def __str__(self):
        return self.tag_name
