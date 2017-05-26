from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Type(models.Model):
    name = models.TextField()
    StrongAgainst = models.TextField(null = True)
    WeakAgainst = models.TextField(null = True)
    InmuneTo = models.TextField(null = True)

    def __unicode__(self):
        return self.name

class Move(models.Model):
    name = models.TextField(null = True)
    effect = models.TextField()

    def __unicode__(self):
        return self.name

class Hability(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name

class HabilitySet(models.Model):
    habs = models.ForeignKey(Hability, null = True)


class Pokemon(models.Model):
    name = models.TextField()
    stats = models.TextField()
    description = models.TextField()
    evolves_from = models.TextField(null=True)
    evolves_to = models.TextField(null=True)
    habilityset = models.ForeignKey(HabilitySet, null = True)
    pokemontype = models.ForeignKey(Type, null = True)


    def __unicode__(self):
        return self.name

class PokemonReview(models.Model):
    ReviewText = models.TextField()
    user = models.ForeignKey(User, default=1)
    pokemon = models.ForeignKey(Pokemon)
    userlocation = models.TextField(max_length = 100, null = True)
