# 🧠 Simulateur de Dilemmes Éthiques

Ce projet Django permet de simuler des dilemmes éthiques interactifs. L’utilisateur explore des scénarios, fait des choix, découvre leurs conséquences et visualise leur impact moral à l’aide d’un graphique circulaire.

---

## 📦 Fonctionnalités

- Liste de scénarios éthiques
- Page de détail pour chaque dilemme
- Formulaire de vote pour choisir une option
- Affichage des conséquences et du score éthique
- Jauge circulaire pour visualiser le score
- Interface claire et responsive avec Bootstrap

---

## 🛠️ Technologies utilisées

- Python 3
- Django
- Matplotlib (pour les graphiques)
- Bootstrap 5
- HTML / CSS
- JSONField (pour stocker les choix, conséquences et scores)

---

## 📁 Structure du projet
```
simulateur_ethique/ 
├── ethique_simulateur/
├── scenarios/
│ ├── models.py 
│ ├── views.py
│ ├── forms.py
│ ├── urls.py 
│ ├── templatetags/ 
│ │ ├── custom_filters.py
│ └── templates/ 
│   └── scenarios/ 
│   ├── scenario_list.html 
│   ├── scenario_detail.html
│   └── result.html
├── manage.py 
└── README.md
```

## 🧱 Modèle `Scenario`

```python
class Scenario(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    choices = models.JSONField()
    consequences = models.JSONField()
    ethical_scores = models.JSONField()
    selected_choice = models.CharField(max_length=255, blank=True, null=True)
```

## 📝 Formulaire VoteForm

```python
class VoteForm(forms.Form):
    choice = forms.ChoiceField(widget=forms.RadioSelect)
```

## 📊 Fonction generate_gauge(score)
Crée une jauge circulaire avec une aiguille pointée sur le score éthique :
```python

def generate_gauge(score):
    # Crée un graphique circulaire avec matplotlib
    # Encode l’image en base64 pour l’afficher dans le HTML
    return graphic

```

## 🌐 Routes

```python
urlpatterns = [
    path('', views.scenario_list, name='scenario_list'),
    path('<int:pk>/', views.scenario_detail, name='scenario_detail'),
]
```
## 🚀 Lancer le projet

1. Installer les dépendances :

```python

pip install django matplotlib
```
2. Appliquer les migrations :

```python
python manage.py makemigrations
python manage.py migrate
```
3. Lancer le serveur :

```python
python manage.py runserver
```

4. Accéder à l’app : http://127.0.0.1:8000

---

## 🎨 Personnalisation

.   Le fond peut être modifié dans les templates avec bg-secondary, bg-dark, ou via CSS.

.   Les couleurs de la jauge peuvent être ajustées dans generate_gauge(score).

## 📌 À venir

.   Profil moral basé sur plusieurs choix

.   Ajout de scénarios via l’interface admin

.   Système de classement ou historique des décisions

---

## 📄 Licence

Ce projet est sous licence MIT. Vous pouvez l’utiliser, le modifier et le partager librement, à condition de conserver les mentions d’origine.

