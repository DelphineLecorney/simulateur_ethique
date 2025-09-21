from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('scenarios/', views.scenario_list, name='scenario_list'),
    path('scenarios/<int:pk>/', views.scenario_detail, name='scenario_detail'),

    path('parcours/', views.parcours_list, name='parcours_list'),
    path('parcours/<int:parcours_id>/start/', views.parcours_start, name='parcours_start'),
    path('parcours/step/', views.parcours_step, name='parcours_step'),
    path('parcours/result/', views.parcours_result, name='parcours_result'),
    path('parcours/reset/', views.reset_parcours, name='reset_parcours'),

]
