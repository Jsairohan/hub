# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-30 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='PHID',
            field=models.SlugField(editable=False, null=True),
        ),
    ]
