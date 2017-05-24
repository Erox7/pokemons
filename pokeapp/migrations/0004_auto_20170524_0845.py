# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokeapp', '0003_pokemonreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonreview',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='type',
            name='InmuneTo',
            field=models.TextField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='pokemonreview',
            unique_together=set([('pokemon', 'user')]),
        ),
    ]
