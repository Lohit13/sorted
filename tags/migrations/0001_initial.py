# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Btech1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Btech2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Btech3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Btech4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagname', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tagset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.ForeignKey(to='tags.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=50, blank=True)),
                ('lname', models.CharField(max_length=50, blank=True)),
                ('email', models.CharField(max_length=100, blank=True)),
                ('batch', models.CharField(max_length=50, blank=True)),
                ('phno', models.BigIntegerField(max_length=10, blank=True)),
                ('role', models.BooleanField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tagset',
            name='user',
            field=models.ForeignKey(to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech4',
            name='user1',
            field=models.ForeignKey(related_name=b'4a', to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech4',
            name='user2',
            field=models.ForeignKey(related_name=b'4b', to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech3',
            name='user1',
            field=models.ForeignKey(related_name=b'3a', to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech3',
            name='user2',
            field=models.ForeignKey(related_name=b'3b', to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech2',
            name='user1',
            field=models.ForeignKey(related_name=b'2a', to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech2',
            name='user2',
            field=models.ForeignKey(related_name=b'2b', to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech1',
            name='user1',
            field=models.ForeignKey(related_name=b'1a', to='tags.Userprofile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='btech1',
            name='user2',
            field=models.ForeignKey(related_name=b'1b', to='tags.Userprofile'),
            preserve_default=True,
        ),
    ]
