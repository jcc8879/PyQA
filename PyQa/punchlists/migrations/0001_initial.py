# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('browser_name', models.CharField(max_length=200)),
                ('browser_ver', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reported_date', models.DateTimeField(verbose_name=b'date published')),
                ('url', models.CharField(max_length=500)),
                ('issue_text', models.CharField(max_length=5000)),
                ('notes', models.CharField(max_length=5000)),
                ('browser', models.ForeignKey(to='punchlists.Browser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Punchlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('punchlist_name', models.CharField(max_length=200)),
                ('punchlist_date', models.DateTimeField(verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reporter_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='issue',
            name='os',
            field=models.ForeignKey(to='punchlists.OS'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='punchlist',
            field=models.ForeignKey(to='punchlists.Punchlist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='reporter',
            field=models.ForeignKey(to='punchlists.Reporter'),
            preserve_default=True,
        ),
    ]
