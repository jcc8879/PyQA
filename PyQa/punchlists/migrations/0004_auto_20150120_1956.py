# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punchlists', '0003_auto_20150114_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.CharField(max_length=5000)),
                ('note_date', models.DateTimeField(auto_now=True)),
                ('issue', models.ForeignKey(to='punchlists.Issue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='issue',
            name='notes',
        ),
    ]
