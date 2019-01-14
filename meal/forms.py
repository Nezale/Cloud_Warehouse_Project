from django import forms


class MealForm(forms.Form):
    quantity = forms.IntegerField(label="Quantity")
