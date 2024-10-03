from django import forms
from .models import Product, Category, Profession, Colours


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        colours = Colours.objects.all()
        profession = Profession.objects.all()

        # Get friendly names of categories
        #https://medium.com/@mattbancroft03/django-crispy-forms-clean-horizontal-multiple-choice-fields-564734738287
        self.fields['category'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[(c.id, c.get_friendly_name()) for c in categories],
            required=False,
        )

        #https://medium.com/@mattbancroft03/django-crispy-forms-clean-horizontal-multiple-choice-fields-564734738287
        self.fields['colours'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[(c.id, c.get_friendly_name()) for c in colours],
            required=False,
        )
        # colour_friendly_names = [(c.id, c.get_friendly_name()) for c in colours]
        # self.fields['colours'].choices = colour_friendly_names

        # Get friendly names of profession
        self.fields['profession'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[(p.id, p.get_friendly_name()) for p in profession],
            required=False,
        )
        # profession_friendly_names = [(p.id, p.get_friendly_name()) for p in profession]
        # self.fields['profession'].choices = profession_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'