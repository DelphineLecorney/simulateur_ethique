from django.core.management.base import BaseCommand
from scenarios.models import Scenario, Parcours

class Command(BaseCommand):
    help = "Peuple la base avec des scénarios éthiques réalistes"

    def handle(self, *args, **kwargs):
        justice_dilemmas = [
    {
        "title": "Punition ou réhabilitation ?",
        "description": "Un jeune homme a commis un vol sans violence. Faut-il l’envoyer en prison ou lui proposer un programme de réinsertion ?",
        "choices": ["Prison ferme", "Réinsertion encadrée", "Sanction communautaire"],
        "consequences": {
            "Prison ferme": "Risque de récidive élevé",
            "Réinsertion encadrée": "Coût élevé mais meilleure réintégration",
            "Sanction communautaire": "Accepté par la société mais peu dissuasif"
        },
        "ethical_scores": {
            "Prison ferme": 30,
            "Réinsertion encadrée": 80,
            "Sanction communautaire": 60
        }
    },
    {
        "title": "Justice pour tous ?",
        "description": "Une personne sans papiers est victime d’un vol. Elle hésite à porter plainte.",
        "choices": ["Encourager à porter plainte", "Ne pas intervenir", "Alerter les autorités discrètement"],
        "consequences": {
            "Encourager à porter plainte": "Risque d’expulsion",
            "Ne pas intervenir": "Injustice non réparée",
            "Alerter les autorités discrètement": "Protection mais incertitude"
        },
        "ethical_scores": {
            "Encourager à porter plainte": 70,
            "Ne pas intervenir": 20,
            "Alerter les autorités discrètement": 60
        }
    },
    {
        "title": "Égalité ou équité ?",
        "description": "Une école reçoit des fonds publics. Faut-il les répartir également entre tous les élèves ou favoriser ceux en difficulté ?",
        "choices": ["Répartition égale", "Priorité aux élèves en difficulté", "Répartition selon mérite"],
        "consequences": {
            "Répartition égale": "Justice formelle mais inégalités persistantes",
            "Priorité aux élèves en difficulté": "Soutien ciblé mais sentiment d’injustice",
            "Répartition selon mérite": "Motivation mais exclusion des plus fragiles"
        },
        "ethical_scores": {
            "Répartition égale": 50,
            "Priorité aux élèves en difficulté": 80,
            "Répartition selon mérite": 40
        }
    },
    {
        "title": "Témoigner contre un proche ?",
        "description": "Tu sais qu’un ami a commis une fraude. Tu es convoqué comme témoin.",
        "choices": ["Témoigner honnêtement", "Mentir pour le protéger", "Refuser de témoigner"],
        "consequences": {
            "Témoigner honnêtement": "Perte d’amitié mais respect de la loi",
            "Mentir pour le protéger": "Risque légal",
            "Refuser de témoigner": "Suspicion et pression"
        },
        "ethical_scores": {
            "Témoigner honnêtement": 90,
            "Mentir pour le protéger": 20,
            "Refuser de témoigner": 50
        }
    },
    {
        "title": "Justice médiatique ?",
        "description": "Un suspect est accusé publiquement avant son procès. Tu es journaliste.",
        "choices": ["Publier les accusations", "Attendre le verdict", "Publier avec réserve"],
        "consequences": {
            "Publier les accusations": "Sensationnalisme mais atteinte à la présomption d’innocence",
            "Attendre le verdict": "Respect de la justice mais perte d’audience",
            "Publier avec réserve": "Équilibre mais critiques des deux camps"
        },
        "ethical_scores": {
            "Publier les accusations": 30,
            "Attendre le verdict": 80,
            "Publier avec réserve": 60
        }
    }
];environment_dilemmas = [
    {
        "title": "Travailler pour une entreprise polluante ?",
        "description": "Tu viens d’obtenir un emploi bien payé, mais l’entreprise est connue pour ses pratiques polluantes.",
        "choices": ["Accepter le poste", "Refuser", "Négocier des pratiques plus vertes"],
        "consequences": {
            "Accepter le poste": "Sécurité financière mais impact environnemental",
            "Refuser": "Perte d’opportunité mais cohérence éthique",
            "Négocier": "Effort louable mais incertain"
        },
        "ethical_scores": {
            "Accepter le poste": 40,
            "Refuser": 80,
            "Négocier": 60
        }
    },
    {
        "title": "Faut-il interdire les SUV en ville ?",
        "description": "Les SUV sont polluants et encombrants, mais très populaires.",
        "choices": ["Interdire", "Taxer", "Sensibiliser"],
        "consequences": {
            "Interdire": "Réduction de pollution mais rejet social",
            "Taxer": "Changement progressif mais inégal",
            "Sensibiliser": "Effet lent mais durable"
        },
        "ethical_scores": {
            "Interdire": 70,
            "Taxer": 60,
            "Sensibiliser": 80
        }
    },
    {
        "title": "Manger local ou bio ?",
        "description": "Tu veux réduire ton empreinte écologique. Faut-il privilégier le local ou le bio ?",
        "choices": ["Local", "Bio", "Les deux"],
        "consequences": {
            "Local": "Moins de transport mais parfois moins durable",
            "Bio": "Respect de la nature mais importé",
            "Les deux": "Idéal mais coûteux"
        },
        "ethical_scores": {
            "Local": 70,
            "Bio": 75,
            "Les deux": 90
        }
    },
    {
        "title": "Voyager en avion pour les vacances ?",
        "description": "Tu rêves de partir loin, mais l’avion est très polluant.",
        "choices": ["Partir en avion", "Choisir une destination locale", "Compenser les émissions"],
        "consequences": {
            "Partir en avion": "Plaisir personnel mais impact fort",
            "Destination locale": "Moins exotique mais responsable",
            "Compenser": "Bonne intention mais efficacité discutée"
        },
        "ethical_scores": {
            "Partir en avion": 30,
            "Destination locale": 80,
            "Compenser": 60
        }
    },
    {
        "title": "Imposer le tri des déchets ?",
        "description": "Certaines personnes refusent de trier leurs déchets. Faut-il rendre le tri obligatoire ?",
        "choices": ["Obligatoire", "Incitatif", "Libre choix"],
        "consequences": {
            "Obligatoire": "Efficace mais autoritaire",
            "Incitatif": "Moins contraignant mais moins rapide",
            "Libre choix": "Respect des libertés mais faible impact"
        },
        "ethical_scores": {
            "Obligatoire": 80,
            "Incitatif": 60,
            "Libre choix": 40
        }
    }
]



        parcours = Parcours.objects.create(
            title="Justice",
            description="Explore les dilemmes liés à la justice sociale."
        )

        for data in justice_dilemmas:
            scenario = Scenario.objects.create(
                title=data["title"],
                description=data["description"],
                choices=data["choices"],
                consequences=data["consequences"],
                ethical_scores=data["ethical_scores"]
            )
            parcours.scenarios.add(scenario)

        parcours_env = Parcours.objects.create(
            title="Environnement",
            description="Explore les dilemmes liés à l’écologie et à la responsabilité environnementale."
        )

        for data in environment_dilemmas:
            scenario = Scenario.objects.create(
                title=data["title"],
                description=data["description"],
                choices=data["choices"],
                consequences=data["consequences"],
                ethical_scores=data["ethical_scores"]
            )
            parcours_env.scenarios.add(scenario)
