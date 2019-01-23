from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from meal.decorators import group_required
from django.urls import reverse

from .models import Component
from component.forms import ComponentForm


@group_required('pracownik')
def index(request):
    components = Component.objects.order_by('-name').all()
    context = {'components': components, }
    return HttpResponse(render(request, 'indexComponent.html', context))


@group_required('pracownik')
def details(request, id):
    component = get_object_or_404(Component, pk=id)
    context = {'component': component,
               'component_fields': component._meta.get_fields()}
    return render(request, 'componentDetail.html', context)


@group_required('pracownik')
def update_component(request, id):
    component = get_object_or_404(Component, pk=id)
    form = ComponentForm()
    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            messages.info(request, "Component has been successfully updated")
            return render(request, 'updateComponent.html', {'form': form})
        else:
            return render(request, 'updateComponent.html', {'form': form})
    else:
        return render(request, 'updateComponent.html', {'form': form})


@group_required('pracownik')
def delete_component(request, id):
    component = get_object_or_404(Component, pk=id)
    component.delete()
    messages.info(request, "Component has been deleted")
    return redirect('/component/')


@group_required('pracownik')
def add_component(request):
    form = ComponentForm()
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            form = ComponentForm()
            messages.info(request, "Component has been successfully added")
            return render(request, 'addComponent.html', {'form': form})
        else:
            return render(request, 'addComponent.html', {'form': form})
    else:
        return render(request, 'addComponent.html', {'form': form})
