from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from products.models import Product
from profiles.models import UserProfile


# Create your models here.
class ProductReview(models.Model):
    class Meta:
        verbose_name_plural = 'Product Reviews'
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(blank=True, null=True)
    # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model/12026867#12026867
    rating = models.IntegerField(default=1,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    date_added = models.DateTimeField(default=timezone.now, editable=False)
