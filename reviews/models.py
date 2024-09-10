from django.db import models
from django.utils import timezone

from products.models import Product
from profiles.models import UserProfile


# Create your models here.
class ProductReview(models.Model):
    class Meta:
        verbose_name_plural = 'Product Reviews'
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now, editable=False)
