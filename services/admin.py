from django.contrib import admin
from .models import Spa, Entry, Staff, Massage


@admin.register(Spa)
class SpaAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'body',
                    'length',
                    'price']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'phone',
                    'email']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['staff',
                    'spa',
                    'owner',
                    'date_time']


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'body',
                    'length',
                    'price']
