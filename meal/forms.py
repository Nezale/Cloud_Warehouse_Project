from django import forms
from .models import Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['components', 'name', 'price', 'meal_type', 'quantity', 'description']

    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 1
        self.fields['quantity'].widget.attrs['min'] = 1
