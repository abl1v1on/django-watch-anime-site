# Generated by Django 5.0.2 on 2024-02-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(default='', upload_to='post_cover/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]