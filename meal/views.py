from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Meal


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


def results(request,id):
    response = "You are looking at the result of meal %s"
    return HttpResponse(response % id)

