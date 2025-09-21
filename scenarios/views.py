from django.shortcuts import render, get_object_or_404, redirect
from .models import Scenario, Parcours
from .forms import VoteForm
import matplotlib.pyplot as plt

def home(request):
    return render(request, 'scenarios/home.html')

def scenario_list(request):
    scenarios = Scenario.objects.all()
    return render(request, 'scenarios/scenario_list.html', {'scenarios': scenarios})

def parcours_list(request):
    parcours = Parcours.objects.all()
    return render(request, 'scenarios/parcours_list.html', {'parcours_list': parcours})


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
            score = scenario.ethical_scores.get(selected, 0)
            consequence = scenario.consequences.get(selected)
            graphic = generate_gauge(score)

            if score < 34:
                moral_zone = "🔴 Choix égoïste ou risqué"
            elif score < 67:
                moral_zone = "🟠 Choix nuancé ou pragmatique"
            else:
                moral_zone = "🟢 Choix altruiste ou responsable"
            
            return render(request, 'scenarios/result.html', {
                'scenario': scenario,
                'choice': selected,
                'score': score,
                'consequence': consequence,
                'graphic': graphic,
                'moral_zone': moral_zone
            })
        return render(request, 'scenarios/scenario_detail.html', {
    'scenario': scenario,
    'form': form
})
    else:
        form = VoteForm()
        form.fields['choice'].choices = choices

    return render(request, 'scenarios/scenario_detail.html', {
        'scenario': scenario,
        'form': form
    })

def generate_gauge(score):
    import matplotlib.pyplot as plt
    import numpy as np
    import io, base64

    if score is None:
        score = 0

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    zones = [(0, 33, 'red'), (33, 66, 'orange'), (66, 100, 'green')]
    for start, end, color in zones:
        ax.barh(1, (end - start) * np.pi / 100, left=start * np.pi / 100, height=1, color=color, alpha=0.6)

    angle = score * np.pi / 100
    ax.plot([angle, angle], [0, 1], color='black', linewidth=3)
 
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_ylim(0, 1.2)
    ax.set_title(f'Score éthique : {score}', fontsize=14)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    plt.close(fig)
    return graphic

def parcours_start(request, parcours_id):
    parcours = get_object_or_404(Parcours, pk=parcours_id)
    request.session['parcours'] = {
        'id': parcours.id,
        'scenarios': [s.id for s in parcours.scenarios.all()],
        'current': 0,
        'scores': []
    }
    return redirect('parcours_step')


def parcours_step(request):
    parcours_data = request.session.get('parcours')
    if not parcours_data:
        return redirect('parcours_start')

    current_index = parcours_data['current']
    scenario_id = parcours_data['scenarios'][current_index]
    scenario = Scenario.objects.get(id=scenario_id)

    choices = [(c, c) for c in scenario.choices]
    form = VoteForm(request.POST or None)
    form.fields['choice'].choices = choices

    if request.method == 'POST' and form.is_valid():
        selected = form.cleaned_data['choice']
        score = scenario.ethical_scores.get(selected)
        parcours_data['scores'].append(score)
        parcours_data['current'] += 1
        request.session['parcours'] = parcours_data

        if parcours_data['current'] >= len(parcours_data['scenarios']):
            return redirect('parcours_result')
        else:
            return redirect('parcours_step')

    return render(request, 'scenarios/parcours_step.html', {
        'scenario': scenario,
        'form': form,
        'step': current_index + 1,
        'total': len(parcours_data['scenarios'])
    })

def parcours_result(request):
    parcours_data = request.session.get('parcours')
    scores = parcours_data['scores']
    average = sum(scores) / len(scores)

    if average > 70:
        profile = "Authentique"
        description = "Tu fais preuve d'une grande cohérence morale, même face à des choix difficiles."
    elif average > 40:
        profile = "Ambivalent"
        description = "Tu cherches l'équilibre entre principes et pragmatisme, avec des nuances dans tes décisions."
    else:
        profile = "Stratégique"
        description = "Tu privilégies les résultats ou les relations, parfois au détriment de la rigueur éthique."


    return render(request, 'scenarios/parcours_result.html', {
        'scores': scores,
        'average': average,
        'profile': profile,
        'description': description,
        'total': len(parcours_data['scenarios']),
    })


def reset_parcours(request):
    if 'parcours' in request.session:
        del request.session['parcours']
    return redirect('parcours_list')