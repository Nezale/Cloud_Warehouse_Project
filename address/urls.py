from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
handler404 = views.handler404
handler500 = views.handler500