from django.contrib import admin
from .models import BeddingsProduct, Offer

# Register your models here.
class BeddingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Offer, OfferAdmin)
admin.site.register(BeddingsProduct, BeddingsAdmin)

