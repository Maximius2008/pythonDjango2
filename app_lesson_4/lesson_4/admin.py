from django.contrib import admin
from .models import Advertisement
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'description', 'auction', 'created_at', 'updated_at', 'user', 'image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, queryset):
        queryset.update(auction=False)

    @admin.action(description='добавить возможность торга')
    def make_auction_as_false(self, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)