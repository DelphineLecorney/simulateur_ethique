import factory
from scenarios.models import Scenario, Parcours


class ScenarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Scenario

    title = factory.Faker("sentence", nb_words=5)
    description = factory.Faker("paragraph", nb_sentences=2)
    choices = ["Option A", "Option B", "Option C"]
    consequences = {
        "Option A": "Conséquence de A",
        "Option B": "Conséquence de B",
        "Option C": "Conséquence de C"
    }
    ethical_scores = {
        "Option A": 30,
        "Option B": 60,
        "Option C": 90
    }

class ParcoursFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Parcours

    title = factory.Faker("word")
    description = factory.Faker("paragraph", nb_sentences=1)

    @factory.post_generation
    def scenarios(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for scenario in extracted:
                self.scenarios.add(scenario)
        else:
            self.scenarios.add(
                ScenarioFactory(),
                ScenarioFactory(),
                ScenarioFactory()
            )
