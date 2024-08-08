from django.contrib import admin
from .models import Product, Category, Profession, Colours

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ColoursAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProfessionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Colours, ColoursAdmin)