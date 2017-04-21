# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habilityset',
            name='name',
        ),
        migrations.AddField(
            model_name='habilityset',
            name='habilityid',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='habilityset',
            name='habs',
            field=models.ForeignKey(to='pokeapp.Hability', null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='habilityset',
            field=models.ForeignKey(to='pokeapp.HabilitySet', null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='pokemontype',
            field=models.ForeignKey(to='pokeapp.Type', null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='StrongAgainst',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='WeakAgainst',
            field=models.TextField(null=True),
        ),
    ]
