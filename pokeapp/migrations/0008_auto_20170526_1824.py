# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0007_pokemonreview_userlocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonreview',
            name='userLocation',
        ),
        migrations.AddField(
            model_name='pokemonreview',
            name='userlocation',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
