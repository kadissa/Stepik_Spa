# Generated by Django 4.0.4 on 2022-05-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_spa_slag'),
    ]

    operations = [
        migrations.AddField(
            model_name='spa',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='spa',
            name='slag',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
