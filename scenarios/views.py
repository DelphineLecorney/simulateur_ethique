from django.shortcuts import render, get_object_or_404
from .models import Scenario
from .forms import VoteForm
import matplotlib.pyplot as plt
import io
import base64


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
            graphic = generate_score_graph(score)
            
            return render(request, 'scenarios/result.html', {
                'scenario': scenario,
                'choice': selected,
                'score': score,
                'consequence': consequence,
                'graphic': graphic
            })

    else:
        form = VoteForm()
        form.fields['choice'].choices = choices

    return render(request, 'scenarios/scenario_detail.html', {
        'scenario': scenario,
        'form': form
    })

def generate_score_graph(score):
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.bar(['Score éthique'], [score], color='green')
    ax.set_ylim(0, 100)
    ax.set_ylabel('Score')
    ax.set_title('Impact éthique')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    return graphic

