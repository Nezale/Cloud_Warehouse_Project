from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.my_profile, name='my_profile'),
]
