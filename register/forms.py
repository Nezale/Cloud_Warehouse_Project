from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required.')
    last_name = forms.CharField(max_length=30, help_text='Required.')
    email = forms.EmailField(max_length=100, help_text='Required.')
    phone_number = forms.DecimalField(max_digits=12, help_text='Required.')
    city = forms.CharField(max_length=100, help_text='Required.')
    zip_code = forms.CharField(max_length=100, help_text='Required.')
    state = forms.CharField(max_length=100, help_text='Required.')
    street = forms.CharField(max_length=100, help_text='Required.')
    company_name = forms.CharField(max_length=100, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name', 'email', 'phone_number',
                  'city', 'zip_code', 'state',
                  'street', 'company_name')