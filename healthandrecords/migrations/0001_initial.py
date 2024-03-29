# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-30 08:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bpmmeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_code', models.IntegerField(null=True)),
                ('diastolic', models.FloatField(null=True)),
                ('systolic', models.FloatField(null=True)),
                ('pulse', models.FloatField(null=True)),
                ('sent_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes_param', models.TextField(null=True)),
                ('heart_score_param', models.TextField(null=True)),
                ('hyper_score_param', models.TextField(null=True)),
                ('h_per_param', models.TextField(null=True)),
                ('obesity', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='evaluation_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=30, null=True)),
                ('weight', models.FloatField(verbose_name=True)),
                ('h_feet', models.IntegerField(null=True)),
                ('h_inches', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('smoker', models.CharField(max_length=30, null=True)),
                ('bp_systolic', models.CharField(max_length=30, null=True)),
                ('bp_diastolic', models.CharField(max_length=30, null=True)),
                ('employment', models.CharField(max_length=30, null=True)),
                ('anualincome', models.CharField(max_length=30, null=True)),
                ('maritial_status', models.CharField(max_length=30, null=True)),
                ('housing_status', models.CharField(max_length=30, null=True)),
                ('drinker', models.CharField(max_length=30, null=True)),
                ('health_condition', models.CharField(max_length=30, null=True)),
                ('eat_vegetables', models.CharField(max_length=30, null=True)),
                ('hospital_screening', models.CharField(max_length=30, null=True)),
                ('family_diabetes', models.CharField(max_length=30, null=True)),
                ('ethnicity', models.CharField(max_length=30, null=True)),
                ('hypertension', models.CharField(max_length=30, null=True)),
                ('waist_circumference', models.CharField(max_length=30, null=True)),
                ('diabetes', models.CharField(max_length=30, null=True)),
                ('exercise', models.CharField(max_length=30, null=True)),
                ('geostational_diabetes', models.CharField(max_length=30, null=True)),
                ('treated_for_systolic_bp', models.CharField(max_length=30, null=True)),
                ('hdl_level', models.CharField(max_length=30, null=True)),
                ('total_cholestoral', models.CharField(max_length=30, null=True)),
                ('blood_glucose', models.CharField(max_length=30, null=True)),
                ('bmr', models.FloatField(blank=True, null=True)),
                ('cardiac', models.CharField(max_length=30, null=True)),
                ('obesity', models.CharField(max_length=30, null=True)),
                ('blood_group', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hos_id', models.AutoField(primary_key=True, serialize=False)),
                ('hosp', models.CharField(max_length=300)),
                ('product', models.CharField(max_length=300)),
                ('covers', models.CharField(max_length=300)),
                ('h_url', models.CharField(max_length=300)),
                ('p_url', models.CharField(max_length=300)),
                ('h_lat', models.FloatField(blank=True, null=True)),
                ('h_log', models.FloatField(blank=True, null=True)),
                ('price', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Risk_sore',
            fields=[
                ('score_id', models.AutoField(primary_key=True, serialize=False)),
                ('diabetes_score', models.IntegerField(null=True)),
                ('heart_score', models.IntegerField(null=True)),
                ('hyper_score', models.IntegerField(null=True)),
                ('h_per', models.IntegerField(null=True)),
                ('bmi', models.FloatField(null=True)),
                ('updated_0n', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Today_hel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_0n', models.DateField(blank=True)),
                ('systo', models.IntegerField()),
                ('diasto', models.IntegerField()),
                ('gluc', models.IntegerField()),
                ('helath_hdl', models.IntegerField(null=True)),
                ('health_tc', models.IntegerField(null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
