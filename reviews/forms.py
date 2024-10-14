from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ('product', 'user_profile', 'rating')
        def clean_rating(self):
            rating = self.cleaned_data.get('rating')
            if not rating:
                raise forms.ValidationError("Please select a rating.")
            return rating

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
