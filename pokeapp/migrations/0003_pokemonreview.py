# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0002_auto_20170421_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name=b'Rating(Stars)', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')])),
                ('ReviewText', models.TextField()),
                ('pokemon', models.ForeignKey(to='pokeapp.Pokemon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
