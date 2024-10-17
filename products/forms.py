from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Profession, Colours


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('rating',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        colours = Colours.objects.all()
        professions = Profession.objects.all()

        # Get friendly names of categories
        # https://medium.com/@mattbancroft03/django-crispy-forms-clean-horizontal-multiple-choice-fields-564734738287 # noqa
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        # Set choices with model names
        # https://docs.djangoproject.com/en/5.1/ref/forms/fields/#modelmultiplechoicefield
        self.fields['colours'] = forms.ModelMultipleChoiceField(
            queryset=colours,
            widget=forms.CheckboxSelectMultiple,
            required=False,
        )
        self.fields['profession'] = forms.ModelMultipleChoiceField(
            queryset=professions,
            widget=forms.CheckboxSelectMultiple,
            required=False,
        )
        # Assign friendly names to choices directly
        self.fields['colours'].choices = [
            (colour.id, colour.get_friendly_name())
            for colour in colours
            ]
        self.fields['profession'].choices = [
            (profession.id, profession.get_friendly_name())
            for profession in professions
            ]
