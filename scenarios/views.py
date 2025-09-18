from django.shortcuts import render
from .models import Scenario

# def scenario_list(request):
#     scenarios = Scenario.objects.all()
#     return render(request, 'scenarios/scenario_list.html', {'scenarios': scenarios})

def scenario_list(request):
    scenarios = Scenario.objects.all()
    return render(request, 'scenarios/scenario_list.html', {'scenarios': scenarios})
