# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse_lazy,reverse
# Create your models here.# curr_indian_insur       # health_form_hospital
class Indian_insur(models.Model):
    company=models.CharField(max_length=300, null=True)
    plan=models.CharField(max_length=300, null=True)
    min_age=models.FloatField(null=True)
    max_age=models.FloatField(null=True)
    coverage=models.CharField(max_length=300, null=True)
    family=models.CharField(max_length=300, null=True)
    summary=models.CharField(max_length=3600, null=True)
    hosp_room=models.CharField(max_length=300, null=True)
    hosp_sup=models.CharField(max_length=300, null=True)
    daily_cash=models.CharField(max_length=300, null=True)
    pre_hosp=models.CharField(max_length=300, null=True)
    posthosp=models.CharField(max_length=300, null=True)
    day_care=models.CharField(max_length=300, null=True)
    orgon_don=models.CharField(max_length=300, null=True)
    Preventive=models.CharField(max_length=300, null=True)
    Restore=models.CharField(max_length=300, null=True)
    inpatient=models.CharField(max_length=300, null=True)
    Ayush=models.CharField(max_length=300, null=True)
    imgn=models.CharField(max_length=300, null=True)
    urls=models.CharField(max_length=300, null=True)
    pre_wait=models.CharField(max_length=300, null=True)
    nor_wait=models.CharField(max_length=300, null=True)
    max_sum=models.CharField(max_length=300, null=True)
    sumassured=models.CharField(max_length=300, null=True)
    def get_absolute_url(self):
        return reverse('insuranceandcygen:indiinsurance', kwargs={'slug': self.urls})
