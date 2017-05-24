# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0004_auto_20170524_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
