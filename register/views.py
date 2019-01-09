#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.db import models
from django.shortcuts import redirect, render
from address.models import Address
from django.contrib.auth import login, authenticate

def register_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.customer.phone_number = form.cleaned_data.get('phone_number')
            user.customer.company_name = form.cleaned_data.get('company_name')
            user.save()

            city = form.cleaned_data.get('city')
            zip_code = form.cleaned_data.get('zip_code')
            state = form.cleaned_data.get('state')
            street = form.cleaned_data.get('street')

            address = Address.objects.create(city=city,
                    zip_code=zip_code, state=state, street=street)

            user.customer.address = address
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)
            login(request, user)

            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
