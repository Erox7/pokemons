from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Type(models.Model):
    name = models.TextField()
    StrongAgainst = models.TextField(null = True)
    WeakAgainst = models.TextField(null = True)
    InmuneTo = models.TextField(null = True)

class Move(models.Model):
    effect = models.TextField()

class Hability(models.Model):
    name = models.TextField()
    description = models.TextField()

class HabilitySet(models.Model):
    habilityid = models.IntegerField(default = 1)
    habs = models.ForeignKey(Hability, null = True)

class Pokemon(models.Model):
    name = models.TextField()
    stats = models.TextField()
    description = models.TextField()
    evolves_from = models.TextField(null=True)
    evolves_to = models.TextField(null=True)
    habilityset = models.ForeignKey(HabilitySet, null = True)
    pokemontype = models.ForeignKey(Type, null = True)

class Review(models.Model):
    RATING_CHOICES = ((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'))
    rating = models.PositiveSmallIntegerField('Rating(Stars)', blank=False,default = 3, choices = RATING_CHOICES)
    ReviewText = models.TextField()
    user = models.ForeignKey(User, default=1)
    class Meta:
        abstract = True

class PokemonReview(Review):
    pokemon = models.ForeignKey(Pokemon)
    class Meta:
        unique_together	= ("pokemon", "user")
