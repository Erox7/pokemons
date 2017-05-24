from django.contrib import admin
import models
# Register your models here.
#Pokemon, Type, Move, Hability, HabilitySet
admin.site.register(models.Pokemon)
admin.site.register(models.Type)
admin.site.register(models.Move)
admin.site.register(models.Hability)
admin.site.register(models.HabilitySet)
admin.site.register(models.PokemonReview)
