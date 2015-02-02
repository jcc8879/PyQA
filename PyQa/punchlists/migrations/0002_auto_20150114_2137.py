# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punchlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='notes',
            field=models.CharField(max_length=5000, blank=True),
            preserve_default=True,
        ),
    ]
