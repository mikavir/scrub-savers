from django.contrib import admin

from .models import ProductReview


# Register your models here.
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user_profile',
        'rating',
        'content',
        'date_added',
    )


admin.site.register(ProductReview, ProductReviewAdmin)
