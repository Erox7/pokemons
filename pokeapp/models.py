from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Pokemon(models.Model):
    name = models.TextField();
    stats = models.TextField();
    description = models.TextField();
    evolves_from = models.TextField(null=True);
    evolves_to = models.TextField(null=True);

class Type(models.Model):
    name = models.TextField();

class Move(models.Model):
    effect = models.TextField();

class Hability(models.Model):
    name = models.TextField();
    description = models.TextField();

class HabilitySet(models.Model):
    name = models.TextField();
