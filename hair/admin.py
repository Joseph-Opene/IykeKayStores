from django.contrib import admin
from .models import HairProduct, Offer

# Register your models here.
class HairAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OfferAdmin)
admin.site.register(HairProduct, HairAdmin)