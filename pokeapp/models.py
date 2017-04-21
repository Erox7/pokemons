from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Type(models.Model):
    name = models.TextField();
    StrongAgainst = models.TextField(null = True);
    WeakAgainst = models.TextField(null = True);

class Move(models.Model):
    effect = models.TextField();

class Hability(models.Model):
    name = models.TextField();
    description = models.TextField();

class HabilitySet(models.Model):
    habilityid = models.IntegerField(default = 1);
    habs = models.ForeignKey(Hability, null = True);

class Pokemon(models.Model):
    name = models.TextField();
    stats = models.TextField();
    description = models.TextField();
    evolves_from = models.TextField(null=True);
    evolves_to = models.TextField(null=True);
    habilityset = models.ForeignKey(HabilitySet, null = True);
    pokemontype = models.ForeignKey(Type, null = True);
