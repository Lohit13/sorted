# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20141105_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='btech1',
            name='count',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech2',
            name='count',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech3',
            name='count',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech4',
            name='count',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=True,
        ),
    ]
