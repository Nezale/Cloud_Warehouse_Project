from django import forms
from .models import Component


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'amount', 'price_per_dish', 'component_type', ]

    def __str__(self):
        return self.name
