# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_auto_20141105_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='allocatedBtech1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user1', models.ForeignKey(related_name='5a', to='tags.Userprofile')),
                ('user2', models.ForeignKey(related_name='5b', to='tags.Userprofile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
