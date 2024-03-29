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
            name='activitysecduled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayofweek', models.CharField(max_length=50)),
                ('exercise', models.CharField(max_length=50)),
                ('howtime', models.IntegerField()),
                ('calburnt', models.FloatField()),
                ('createdDate', models.DateTimeField(default=datetime.datetime(2019, 8, 30, 8, 31, 3, 249839))),
                ('isperformed', models.CharField(default='', max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctorpresciption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docname', models.CharField(max_length=300, null=True)),
                ('prescription', models.TextField(null=True)),
                ('patient', models.CharField(max_length=300, null=True)),
                ('createdDate', models.CharField(max_length=50, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='fit_ex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=300, null=True)),
                ('kg_41', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_45', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_50', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_54', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_59', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_64', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_68', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_73', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_77', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_82', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_86', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_91', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_100', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_109', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_118', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_127', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('kg_136', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serving_Size', models.CharField(max_length=300, null=True)),
                ('Calories', models.CharField(max_length=300, null=True)),
                ('Fat', models.CharField(max_length=300, null=True)),
                ('Carbs', models.CharField(max_length=300, null=True)),
                ('Protein', models.CharField(max_length=300, null=True)),
                ('fodd_name', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foodsecd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(null=True)),
                ('breakf', models.CharField(max_length=300, null=True)),
                ('lunch', models.CharField(max_length=300, null=True)),
                ('dinner', models.CharField(max_length=300, null=True)),
                ('secuded', models.DateField(null=True)),
                ('cal_food', models.CharField(max_length=30, null=True)),
                ('ver_son', models.CharField(max_length=30, null=True)),
                ('exerc', models.CharField(max_length=150, null=True)),
                ('durations', models.CharField(max_length=15, null=True)),
                ('editeedon', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicationlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrescriptionDate', models.CharField(max_length=300, null=True)),
                ('MedicationName', models.CharField(max_length=300, null=True)),
                ('Doctor', models.CharField(max_length=300, null=True)),
                ('Dosage', models.CharField(max_length=300, null=True)),
                ('TimesPerDay', models.CharField(max_length=300, null=True)),
                ('WithFood', models.CharField(max_length=300, null=True)),
                ('Reason', models.CharField(max_length=300, null=True)),
                ('Reactions', models.CharField(max_length=300, null=True)),
                ('timmings', models.CharField(max_length=300, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='recipefoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=150, null=True)),
                ('Energy', models.FloatField()),
                ('Protein', models.CharField(max_length=50, null=True)),
                ('Carbohydrates', models.CharField(max_length=50, null=True)),
                ('Fiber', models.CharField(max_length=50, null=True)),
                ('Fat', models.CharField(max_length=50, null=True)),
                ('Cholesterol', models.CharField(max_length=50, null=True)),
                ('Sodium', models.CharField(max_length=50, null=True)),
                ('Zinc', models.CharField(max_length=50, null=True)),
                ('Potassium', models.CharField(max_length=50, null=True)),
                ('Calcium', models.CharField(max_length=50, null=True)),
                ('VitaminA', models.CharField(max_length=50, null=True)),
                ('Magnesium', models.CharField(max_length=50, null=True)),
                ('Phosphorus', models.CharField(max_length=50, null=True)),
                ('FolicAcid', models.CharField(max_length=50, null=True)),
                ('specifirecipe', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='setgoalsd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('targetnumberkg', models.IntegerField()),
                ('targetdays', models.IntegerField()),
                ('change_type', models.CharField(max_length=50, null=True)),
                ('calneeded', models.FloatField(null=True)),
                ('editeedon', models.DateField(default=datetime.date.today, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='transfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_gain', models.IntegerField(null=True)),
                ('gain_time', models.IntegerField(null=True)),
                ('activity', models.IntegerField(null=True)),
                ('activityname', models.CharField(max_length=300, null=True)),
                ('act_time', models.IntegerField(null=True)),
                ('weight_loss', models.IntegerField(null=True)),
                ('loss_time', models.IntegerField(null=True)),
                ('typer', models.CharField(max_length=300, null=True)),
                ('calneeded', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfosummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('PhoneNo', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=250)),
                ('hospitalAddress', models.CharField(max_length=250)),
                ('guardianname', models.CharField(max_length=50)),
                ('ContactNo', models.CharField(max_length=50)),
                ('gAddress', models.CharField(max_length=250)),
                ('Doctorname', models.CharField(max_length=50)),
                ('Doctornumb', models.CharField(max_length=50)),
                ('MaritalStatus', models.CharField(max_length=50)),
                ('EmployedStatus', models.CharField(max_length=50)),
                ('HousingStatus', models.CharField(max_length=50)),
                ('allergy', models.CharField(max_length=250)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='usersfoodsdairy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sluged', models.CharField(max_length=40, unique=True)),
                ('Calories', models.CharField(max_length=50, null=True)),
                ('Fat', models.CharField(max_length=50, null=True)),
                ('Carbs', models.CharField(max_length=50, null=True)),
                ('Protein', models.CharField(max_length=50, null=True)),
                ('fodd_name', models.CharField(max_length=100, null=True)),
                ('wheninday', models.CharField(max_length=50, null=True)),
                ('fooddate', models.DateField(null=True)),
                ('editeedon', models.DateField(auto_now=True, null=True)),
                ('isconsumed', models.CharField(default='', max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
