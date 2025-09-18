from django.urls import path
from . import views

urlpatterns = [
    path('', views.scenario_list, name='scenario_list'),
]
