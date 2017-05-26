# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0005_move_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habilityset',
            name='habilityid',
        ),
        migrations.AlterUniqueTogether(
            name='pokemonreview',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='pokemonreview',
            name='rating',
        ),
    ]
