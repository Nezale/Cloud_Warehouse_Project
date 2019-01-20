from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='component-list'),
    path('<int:id>/detail/', views.details, name='component-details'),
    path('<int:id>/delete/', views.delete_component, name='delete-component'),
    path('<int:id>/update/', views.update_component, name='update-component'),
    path('add/', views.add_component, name='add-component')
]