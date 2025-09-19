from django.shortcuts import render, get_object_or_404
from .models import Scenario
from .forms import VoteForm

def scenario_list(request):
    scenarios = Scenario.objects.all()
    return render(request, 'scenarios/scenario_list.html', {'scenarios': scenarios})

def scenario_detail(request, pk):
    scenario = get_object_or_404(Scenario, pk=pk)

    choices = [(c, c) for c in scenario.choices]

    if request.method == 'POST':
        form = VoteForm(request.POST)
        form.fields['choice'].choices = choices
        if form.is_valid():
            selected = form.cleaned_data['choice']
            scenario.selected_choice = selected
            scenario.save()
            score = scenario.ethical_scores.get(selected)
            consequence = scenario.consequences.get(selected)
            return render(request, 'scenarios/result.html', {
                'scenario': scenario,
                'choice': selected,
                'score': score,
                'consequence': consequence
            })
    else:
        form = VoteForm()
        form.fields['choice'].choices = choices

    return render(request, 'scenarios/scenario_detail.html', {
        'scenario': scenario,
        'form': form
    })
