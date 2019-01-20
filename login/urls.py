from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_login),
    path('raport', views.count_quantity),
    path('logout', views.logout_p)
]
