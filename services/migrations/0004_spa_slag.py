# Generated by Django 4.0.4 on 2022-05-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_dayentry_alter_entry_options_timeentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='spa',
            name='slag',
            field=models.SlugField(default=''),
        ),
    ]
