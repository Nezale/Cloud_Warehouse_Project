from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from meal.models import Meal
from login.models import Raport


# Create your views here.


def main_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        if 'LogInForm' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                user = User.objects.get(id=user.id)
                if request.user.groups.filter(name='pracownik').exists():
                    return render(request, 'pracownik.html', {'form': form, 'mealQuantity': Raport.meal_quantity})

                return render(request, 'indexLogin.html', {'form': form})
            else:
                return render(request, 'indexLogin.html', {'form': form})
        elif 'LogOutForm' in request.POST:
            logout(request)
            form = AuthenticationForm()
            return render(request, 'indexLogin.html', {'form': form})

    else:
        user = request.user.is_authenticated
        if request.user.groups.filter(name='pracownik').exists():
            return render(request, 'pracownik.html', {'form': form, 'mealQuantity': Raport.meal_quantity})
        if user:
            form = AuthenticationForm(data=request.POST)
            return render(request, 'indexLogin.html', {'form': form})
        else:
            form = AuthenticationForm()
            return render(request, 'indexLogin.html', {'form': form})


def count_quantity(request):
    Raport.meal_quantity = Meal.objects.get().quantity
    return redirect('/login')


def logout_p(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'index.html')
