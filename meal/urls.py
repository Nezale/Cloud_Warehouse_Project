from django.urls import path

from . import views

app_name = 'meal'
urlpatterns = [
    path('', views.index, name='meals-list'),
    path('<int:id>/', views.detail, name='detail'),
    path('add/', views.addMeal, name='add-meal'),
    path('<int:id>/delete/', views.delete_meal, name='delete-meal'),
    path('<int:id>/update/', views.update_meal, name='update-meal'),
]

