from django import forms
from .models import Component


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'amount', 'price_per_dish', 'component_type', ]

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(ComponentForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['min'] = 1
        self.fields['price_per_dish'].widget.attrs['min'] = 1,
