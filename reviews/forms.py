from django import forms
from .models import ProductReview
from products.models import Product
from profiles.models import UserProfile
from django.shortcuts import get_object_or_404


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ('product','user_profile')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
