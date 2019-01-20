from django.shortcuts import render


# Create your views here.
def main_page(request):
    if request.user.groups.filter(name='pracownik').exists():
        return render(request, 'pracownik.html')
    else:
        return render(request, 'index.html')
