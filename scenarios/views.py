from django.shortcuts import render, get_object_or_404
from .models import Scenario


def scenario_list(request):
    scenarios = Scenario.objects.all()
    return render(request, 'scenarios/scenario_list.html', {'scenarios': scenarios})

def scenario_detail(request, pk):
    scenario = get_object_or_404(Scenario, pk=pk)
    return render(request, 'scenarios/scenario_detail.html', {'scenario': scenario})