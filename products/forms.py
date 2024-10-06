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
        profession = Profession.objects.all()

        # Get friendly names of categories
        #https://medium.com/@mattbancroft03/django-crispy-forms-clean-horizontal-multiple-choice-fields-564734738287 # noqa
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        self.fields['colours'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[(c.id, c.get_friendly_name()) for c in colours],
            required=False,
        )

        # Get friendly names of profession
        self.fields['profession'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[(p.id, p.get_friendly_name()) for p in profession],
            required=False,
        )

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1' # noqa
