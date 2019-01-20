from django.shortcuts import render
from django.http import HttpResponse

from component.forms import ComponentForm


def add_component(request):
    form = ComponentForm()
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            form = ComponentForm()
            return render(request, 'pracAddComponent.html', {'form': form})
        else:
            return render(request, 'pracAddComponent.html', {'form': form})
    else:
        return render(request, 'pracAddComponent.html', {'form': form})
