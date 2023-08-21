from django.contrib import admin
from .models import Advertisement
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'auction', 'created_at', 'user', 'image']
    list_filter = ['auction', 'created_at']


admin.site.register(Advertisement, AdvertisementAdmin)