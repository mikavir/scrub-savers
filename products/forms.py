from django import forms
from .models import Product, Category, Profession, Colour


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        colour = Colour.objects.all()
        profession = Profession.objects.all()

        # Get friendly names of categories
        categories_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = categories_friendly_names

        # Get friendly names of colours 
        colour_friendly_names = [(c.id, c.get_friendly_name()) for c in colour]
        self.fields['colour'].choices = colour_friendly_names

        # Get friendly names of profession
        profession_friendly_names = [(p.id, p.get_friendly_name()) for p in profession]
        self.fields['profession'].choices = profession_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'