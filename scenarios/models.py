from django.db import models

class Scenario(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    choices = models.JSONField()
    consequences = models.JSONField()
    ethical_scores = models.JSONField()
    selected_choice = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.title

class Parcours(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    scenarios = models.ManyToManyField(Scenario)
