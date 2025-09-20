from django.contrib import admin
from .models import Scenario, Parcours

class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ParcoursAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('scenarios',)

admin.site.register(Scenario, ScenarioAdmin)
admin.site.register(Parcours, ParcoursAdmin)
