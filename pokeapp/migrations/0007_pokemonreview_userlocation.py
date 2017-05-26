# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0006_auto_20170526_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonreview',
            name='userLocation',
            field=models.TextField(null=True),
        ),
    ]
