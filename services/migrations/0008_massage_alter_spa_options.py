# Generated by Django 4.0.4 on 2022-05-08 11:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_spa_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Рекламное описание')),
                ('length', models.PositiveSmallIntegerField(verbose_name='Продолжительность')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Стоимость')),
                ('slag', models.SlugField(blank=True, default='')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Массаж',
                'verbose_name_plural': 'Массаж',
            },
        ),
        migrations.AlterModelOptions(
            name='spa',
            options={'verbose_name': 'Спа', 'verbose_name_plural': 'Спа'},
        ),
    ]
