import pytils
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from Stepik_Spa import settings


class Spa(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    body = RichTextUploadingField(verbose_name='Описание')
    content = RichTextUploadingField(verbose_name='Рекламное описание', default='')
    length = models.PositiveSmallIntegerField(verbose_name='Продолжительность')
    price = models.PositiveSmallIntegerField(verbose_name='Стоимость')
    slag = models.SlugField(null=False, default='', blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        self.slag = pytils.translit.slugify(self.title)
        super(Spa, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Спа'
        verbose_name_plural = 'Спа'

    def __str__(self):
        return self.title


class Massage(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    body = RichTextUploadingField(verbose_name='Описание')
    content = RichTextUploadingField(verbose_name='Рекламное описание', default='')
    length = models.PositiveSmallIntegerField(verbose_name='Продолжительность')
    price = models.PositiveSmallIntegerField(verbose_name='Стоимость')
    slug = models.SlugField(null=False, default='', blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        self.slag = pytils.translit.slugify(self.title)
        super(Massage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массаж'

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Мастер')
    phone = models.CharField(max_length=12, null=True, verbose_name='Телефон')
    email = models.EmailField(null=True)

    class Meta:
        verbose_name_plural = 'Мастера'
        verbose_name = 'Мастер'

    def __str__(self):
        return self.name


class Entry(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Мастер', blank=True)
    spa = models.ForeignKey(Spa, on_delete=models.CASCADE, verbose_name='Программа', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='Клиент')

    date = models.DateField(auto_now_add=True)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class DayEntry(models.Model):
    DAY_CHOICES = [
        ('MO', 'Monday',),
        ('TU', 'Tuesday '),
        ('WE', 'Wednesday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday'),
        ('SA', 'Saturday'),
        ('SU', 'Sunday')
    ]
    day_choice = models.CharField(max_length=2, choices=DAY_CHOICES)
    data = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'День записи'
        verbose_name = 'День записи'


class TimeEntry(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day_entry = models.ForeignKey(DayEntry, on_delete=models.CASCADE)
    time_entry = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Время записи'
