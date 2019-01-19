from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Meal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from google.cloud import storage
# Create your views here.
from component.forms import ComponentForm
from meal.forms import MealForm


def index(request):
    meals = Meal.objects.order_by('-name').all()
    context = {'meals': meals, }
    return HttpResponse(render(request, 'meal/index.html', context))


def detail(request, id):
    meal = get_object_or_404(Meal, pk=id)
    return render(request, 'meal/detail.html', {
        'meal': meal,
        'meal_fields': meal._meta.get_fields()
    })


def results(request, id):
    response = "You are looking at the result of meal %s"
    return HttpResponse(response % id)


def addMeal(request):
    formComponent = ComponentForm()
    formMeal = MealForm()


    if request.method == 'POST':
        if 'authorFormButton' in request.POST:
            form = ComponentForm(request.POST)
            if form.is_valid():
                component = form.save()
                return render(request, 'meal/pracAddMeal.html', {'formComponent': formComponent, 'formMeal': formMeal})
            else:
                return render(request, 'meal/pracAddMeal.html', {'formComponent': form, 'formMeal': formMeal})
        elif 'bookFormButton' in request.POST:
            form = MealForm(request.POST, request.FILES)
            if form.is_valid():
                meal = form.save()
                testurl = meal.description
                return render(request, 'meal/pracAddMeal.html',
                              {'formComponent': formComponent, 'formMeal': formMeal, 'testurl': testurl})
            else:
                return render(request, 'meal/pracAddMeal.html', {'formComponent': form, 'formComponent': formComponent})
    else:
        return render(request, 'meal/pracAddMeal.html', {'formComponent': formComponent, 'formMeal': formMeal})
