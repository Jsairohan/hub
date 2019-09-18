# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from beforelogin.models import User
from datetime import date
# Create your models here.
class Bpmmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    diastolic=models.FloatField(null=True)
    systolic=models.FloatField(null=True)
    pulse=models.FloatField(null=True)

    sent_time=models.DateTimeField(auto_now_add=True,null=True)


# class person_form(models.Model):
#     form_id=models.AutoField(primary_key=True)
#     patient_code = models.IntegerField(null=True)
#     user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
#     age=models.CharField(max_length=300,null=True)
#     hieght=models.IntegerField(null=True)
#     i_feet=models.IntegerField(null=True)
#     i_inches=models.IntegerField(null=True)
#     weight=models.FloatField(null=True)
#     gender=models.CharField(max_length=300,null=True)
#     exercise=models.CharField(max_length=300,null=True)
#     smoker=models.CharField(max_length=300,null=True)
#     drinker=models.CharField(max_length=300,null=True)
#     diabetes=models.CharField(max_length=300,null=True)
#     diastolic=models.CharField(max_length=300,null=True)
#     hypertension=models.CharField(max_length=300,null=True)
#     treated=models.CharField(max_length=300,null=True)
#     hdl=models.IntegerField(null=True)
#     bp=models.IntegerField(null=True)
#     m_status=models.CharField(max_length=300,null=True)
#     h_status=models.CharField(max_length=300,null=True)
#     employe=models.CharField(max_length=300,null=True)
#     a_income=models.IntegerField(null=True)
#     wasit=models.IntegerField(null=True)
#     tc=models.IntegerField(null=True)
#     bg=models.CharField(max_length=300,null=True)
#     eat=models.CharField(max_length=300,null=True)
#     bmi=models.CharField(max_length=300,null=True)
#     f_diabetes=models.CharField(max_length=300,null=True)
#     img_name=models.CharField(max_length=300,null=True)
#     h_cond=models.CharField(max_length=300,null=True)
#     hosp_screen=models.CharField(max_length=300,null=True)
#     feet_inches=models.DecimalField(max_digits=6, decimal_places=2,null=True)
#     updated_at=models.DateTimeField(auto_now_add=True,null=True)
#     bmr = models.FloatField(null=True)





class Today_hel(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    updated_0n = models.DateField(blank=True)
    systo=models.IntegerField()
    diasto=models.IntegerField()
    gluc=models.IntegerField()
    helath_hdl = models.IntegerField(null=True)
    health_tc = models.IntegerField(null=True)

class Hospital(models.Model):
    hos_id=models.AutoField(primary_key=True)
    hosp=models.CharField(max_length=300)
    product=models.CharField(max_length=300)
    covers=models.CharField(max_length=300)
    h_url=models.CharField(max_length=300)
    p_url=models.CharField(max_length=300)
    h_lat=models.FloatField(null=True, blank=True,)
    h_log=models.FloatField(null=True, blank=True,)
    price=models.CharField(max_length=7)




class evaluation_form(models.Model):
    user = models.ForeignKey(User)
    age=models.CharField(max_length=30,null=True)
    weight=models.FloatField(True)
    h_feet=models.IntegerField(null=True)
    h_inches=models.IntegerField(null=True)
    gender=models.CharField(max_length=30,null=True)
    smoker=models.CharField(max_length=30,null=True)
    bp_systolic=models.CharField(max_length=30,null=True)
    bp_diastolic = models.CharField(max_length=30, null=True)
    employment=models.CharField(max_length=30,null=True)
    anualincome=models.CharField(max_length=30,null=True)
    maritial_status=models.CharField(max_length=30,null=True)
    housing_status=models.CharField(max_length=30,null=True)
    drinker=models.CharField(max_length=30,null=True)
    health_condition=models.CharField(max_length=30,null=True)
    eat_vegetables=models.CharField(max_length=30,null=True)
    hospital_screening=models.CharField(max_length=30,null=True)
    family_diabetes=models.CharField(max_length=30,null=True)
    ethnicity = models.CharField(max_length=30,null=True)
    hypertension=models.CharField(max_length=30,null=True)
    waist_circumference=models.CharField(max_length=30,null=True)
    diabetes=models.CharField(max_length=30,null=True)
    exercise = models.CharField(max_length=30, null=True)
    geostational_diabetes = models.CharField(max_length=30, null=True)
    treated_for_systolic_bp=models.CharField(max_length=30,null=True)
    hdl_level=models.CharField(max_length=30,null=True)
    total_cholestoral=models.CharField(max_length=30,null=True)
    blood_glucose=models.CharField(max_length=30,null=True)
    bmr = models.FloatField(null=True,blank=True)
    cardiac = models.CharField(max_length=30,null=True)
    obesity = models.CharField(max_length=30,null=True)
    blood_group = models.CharField(max_length=30, null=True)

    def save(self, *args,**kwargs):
        if all([self.bp_systolic,self.blood_glucose,self.bp_diastolic, self.total_cholestoral, self.hdl_level]):
            update_healthindex = Today_hel()
            update_healthindex.user=self.user
            update_healthindex.diasto = int(float(self.bp_diastolic))
            update_healthindex.gluc=int(float(self.blood_glucose))
            update_healthindex.health_tc= int(float(self.total_cholestoral))
            update_healthindex.systo=int(float(self.bp_systolic))
            update_healthindex.helath_hdl=int(float(self.hdl_level))
            update_healthindex.updated_0n =date.today()
            update_healthindex.save()
        super(evaluation_form,self).save()
class Risk_sore(models.Model):
    #patient_code = models.IntegerField(null=True)
    score_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    diabetes_score=models.IntegerField(null=True)
    heart_score=models.IntegerField(null=True)
    hyper_score=models.IntegerField(null=True)
    h_per=models.IntegerField(null=True)
    bmi = models.FloatField(null=True)
    updated_0n=models.DateField(default=date.today)

class CheckParams(models.Model):
    user = models.ForeignKey(User)
    diabetes_param = models.TextField(null=True)
    heart_score_param = models.TextField(null=True)
    hyper_score_param = models.TextField(null=True)
    h_per_param = models.TextField(null=True)
    obesity = models.CharField(max_length=50,null=True)
    # bmi_param = models.FloatField(null=True)