from django.forms.widgets import CheckboxSelectMultiple
from django import forms

from .models import Stock


class StockForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Stock
        fields = ['brand', 'model', 'note', 'energy_class', 'price']

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple': 'true'})
