# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-09-17 12:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodandacti', '0007_auto_20190917_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysecduled',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 17, 12, 30, 50, 320640)),
        ),
    ]
