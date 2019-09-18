# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4
from django.core.cache import cache
from django.db import IntegrityError
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password
from datetime import date
from beforelogin.models import User
from usermanagement.models import *
from apiforapp.riskupdater import *


# Create your models here.
#
class pocapi(models.Model):
    patient_code = models.IntegerField(null=True, unique=True)
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True)
    phno = models.CharField(unique=True, max_length=150, null=True)
    password = models.CharField(max_length=50, default="cygen@123")
    height = models.FloatField(null=True)
    bloodgroup = models.CharField(max_length=150, null=True)
    gender = models.CharField(max_length=150, null=True)
    age = models.CharField(max_length=150, null=True)
    sluged = models.CharField(max_length=150, null=True)
    weight = models.FloatField(null=True)


@receiver(post_save, sender=pocapi)
def ensure_profile_exist(sender, instance, **kwargs):
    obj = User()
    dict_obj = model_to_dict(instance)
    # print dict_obj
    # dict_obj1={}
    password = make_password(dict_obj["password"])
    obj.password = password
    obj.first_name = dict_obj["name"]
    obj.patient_code = dict_obj["patient_code"]
    obj.phone = dict_obj["phno"]
    obj.email = dict_obj["email"]
    obj.is_verified = True

    obj.sluged = dict_obj["sluged"]
    obj.phone = dict_obj["phno"]
    obj.save()
    vermod = verifcation()
    vermod.user = obj
    vermod.save()
    # User.objects.create(**dict_obj1)

    #                 user_speci='health_details').users_cache_speci()
    # a = Geter_cache(id=user.id).common_cache()


#
#
# class patientevaluation_form(models.Model):
#     patient_code = models.IntegerField()
#     # uid=models.IntegerField(null=True)
#     user = models.ForeignKey(User)
#
#     age = models.CharField(max_length=30, null=True)
#     weight = models.FloatField(True)
#     h_feet = models.IntegerField(null=True)
#     h_inches = models.IntegerField(null=True)
#     gender = models.CharField(max_length=30, null=True)
#     smoker = models.CharField(max_length=30, null=True)
#     bp_systolic = models.CharField(max_length=30, null=True)
#     bp_diastolic = models.CharField(max_length=30, null=True)
#     employment = models.CharField(max_length=30, null=True)
#     anualincome = models.CharField(max_length=30, null=True)
#     maritial_status = models.CharField(max_length=30, null=True)
#     housing_status = models.CharField(max_length=30, null=True)
#     drinker = models.CharField(max_length=30, null=True)
#     health_condition = models.CharField(max_length=30, null=True)
#     eat_vegetables = models.CharField(max_length=30, null=True)
#     hospital_screening = models.CharField(max_length=30, null=True)
#     family_diabetes = models.CharField(max_length=30, null=True)
#     hypertension = models.CharField(max_length=30, null=True)
#     waist_circumference = models.CharField(max_length=30, null=True)
#     diabetes = models.CharField(max_length=30, null=True)
#     exercise = models.CharField(max_length=30, null=True)
#     geostational_diabetes = models.CharField(max_length=30, null=True)
#     treated_for_systolic_bp = models.CharField(max_length=30, null=True)
#     hdl_level = models.CharField(max_length=30, null=True)
#     total_cholestoral = models.CharField(max_length=30, null=True)
#     blood_glucose = models.CharField(max_length=30, null=True)
#     bmr = models.FloatField(null=True)
#
#
# class patientRisk_sore(models.Model):
#     #patient_code = models.IntegerField(null=True)
#     user = models.ForeignKey(User)
#
#     patient_code = models.IntegerField(null=True)
#     diabetes_score=models.IntegerField(null=True)
#     heart_score=models.IntegerField(null=True)
#     hyper_score=models.IntegerField(null=True)
#     h_per=models.IntegerField(null=True)
#     bmi = models.FloatField(null=True)
#     updated_0n=models.DateField(default=date.today)


class glucos(models.Model):
    patient_code = models.IntegerField(null=True)
    bpvalue = models.FloatField(null=True)
    glucose = models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


@receiver(post_save, sender=glucos)
def ensure_glucose_exist(sender, instance, **kwargs):
    pat = Patient.objects.get(patient_code=instance.patient_code)
    print pat.pat_id
    up_evaluform = evaluation_form.objects.filter(user_id=pat.pat_id).last()
    print instance.glucose, "vgvvvvvvvv"
    up_evaluform.blood_glucose = instance.glucose
    up_evaluform.save()


class totalcholestrol(models.Model):
    patient_code = models.IntegerField(null=True)
    cholestrol = models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


@receiver(post_save, sender=totalcholestrol)
def ensure_cholestrol_exist(sender, instance, **kwargs):
    pat = Patient.objects.get(patient_code=instance.patient_code)
    print pat.pat_id
    up_evaluform = evaluation_form.objects.filter(user_id=pat.pat_id).last()
    print instance.cholestrol, "vgvvvvvvvv"
    up_evaluform.total_cholestoral = instance.cholestrol
    up_evaluform.save()
    dict_obj = model_to_dict(up_evaluform)
    xyz = updaterisk(dict_obj)


class oximeter(models.Model):
    patient_code = models.IntegerField(null=True)
    spo = models.FloatField(null=True)
    bpm = models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    # unit=models.CharField(max_length=150,null=True)


class Temperature(models.Model):
    patient_code = models.IntegerField(null=True)
    temperature = models.FloatField(null=True)
    # bpm=models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


class Bpmmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    diastolic = models.FloatField(null=True)
    systolic = models.FloatField(null=True)
    pulse = models.FloatField(null=True)

    sent_time = models.DateTimeField(auto_now_add=True, null=True)


@receiver(post_save, sender=Bpmmeter)
def ensure_Bpm_exist(sender, instance, **kwargs):
    pat = Patient.objects.get(patient_code=instance.patient_code)
    print pat.pat_id
    up_evaluform = evaluation_form.objects.filter(user_id=pat.pat_id).last()
    print instance.systolic, "vgvvvvvvvv"
    # up_evaluform=evaluation_form.objects.filter(user_id=id).last()
    up_evaluform.bp_systolic = instance.systolic
    up_evaluform.bp_diastolic = instance.diastolic
    up_evaluform.save()
    dict_obj = model_to_dict(up_evaluform)

    xyz = updaterisk(dict_obj)


class Hdlmmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    hdl = models.FloatField(null=True)
    unit = models.CharField(max_length=15, null=True)

    sent_time = models.DateTimeField(auto_now_add=True, null=True)


@receiver(post_save, sender=Hdlmmeter)
def ensure_Hdl_exist(sender, instance, **kwargs):
    pat = Patient.objects.get(patient_code=instance.patient_code)
    print pat.pat_id
    up_evaluform = evaluation_form.objects.filter(user_id=pat.pat_id).last()
    print instance.hdl, "vgvvvvvvvv"
    up_evaluform.hdl_level = instance.hdl

    up_evaluform.save()
    dict_obj = model_to_dict(up_evaluform)

    xyz = updaterisk(dict_obj)


# @receiver(post_save, sender=Bpmmeter)
# def ensure_profile_exists1(sender, instance, created, **kwargs):
#         # obj=Health_history()
#     dict_obj = model_to_dict(instance)
#
#     a = get_or_none(person_form, patient_code=dict_obj["patient_code"])
#     if a :
#         a.diastolic=dict_obj.get("bp")
#         a.bp=dict_obj.get("diastolic")
#         # user = get_or_none(User, patient_code=dict_obj["patient_code"])
#         # user = User.objects.get(id=user.id)
#         # dict_obj["user"] = user
#         # #a.patient_code=dict_obj.get("patient_code")
#         a.save()
#     else:
#         person_form.objects.create(**dict_obj)
#
#     print "created on here........."


class Weightmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    # bpm=models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


@receiver(post_save, sender=Weightmeter)
def ensure_Weight_exist(sender, instance, **kwargs):
    pat = Patient.objects.get(patient_code=instance.patient_code)
    print pat.pat_id
    up_evaluform = evaluation_form.objects.filter(user_id=pat.pat_id).last()
    print instance.weight, "vgvvvvvvvv"
    up_evaluform.weight = instance.weight
    up_evaluform.save()
    dict_obj = model_to_dict(up_evaluform)
    xyz = updaterisk(dict_obj)


class Spirometery(models.Model):
    patient_code = models.IntegerField(null=True)
    fvc = models.FloatField(null=True)
    fev = models.FloatField(null=True)
    pef = models.FloatField(null=True)
    fevfvc = models.FloatField(null=True)
    fef25 = models.FloatField(null=True)
    fef50 = models.FloatField(null=True)
    fef75 = models.FloatField(null=True)
    fef2575 = models.FloatField(null=True)

    sent_time = models.DateTimeField(auto_now_add=True, null=True)


class Himobloginmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    hemoglobin = models.FloatField(null=True)
    # bpm=models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


class Hbacmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    hbac = models.FloatField(null=True)
    # bpm=models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


class Ldlmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    ldl = models.FloatField(null=True)
    # bpm=models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


class Totalcolestrolmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    tcl = models.FloatField(null=True)
    # bpm=models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


@receiver(post_save, sender=Totalcolestrolmeter)
def ensure_Totalcolestrol_exist(sender, instance, **kwargs):
    pat = Patient.objects.get(patient_code=instance.patient_code)
    print pat.pat_id
    up_evaluform = evaluation_form.objects.filter(user_id=pat.pat_id).last()
    print instance.tcl, "vgvvvvvvvv"
    up_evaluform.total_cholestoral = instance.tcl
    up_evaluform.save()
    dict_obj = model_to_dict(up_evaluform)
    xyz = updaterisk(dict_obj)


class Triglecyridesmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    tri = models.FloatField(null=True)
    # bpm=models.FloatField(null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)
    unit = models.CharField(max_length=150, null=True)


class Urinemeter(models.Model):
    patient_code = models.IntegerField(null=True)
    bil = models.FloatField(null=True)
    pro = models.FloatField(null=True)
    ket = models.FloatField(null=True)
    leu = models.CharField(max_length=150, null=True)
    ph = models.FloatField(null=True)
    glu = models.FloatField(null=True)
    nit = models.FloatField(null=True)
    # usg = models.FloatField( null=True)
    sent_time = models.DateTimeField(auto_now_add=True, null=True)


class Ecgmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    ECG_File = models.URLField(max_length=150)
    time = models.DateTimeField(auto_now_add=True, null=True)
    # source = models.FileField(upload_to='media/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='documents/', null=True, blank=True)


class EcgNIGmeter(models.Model):
    patient_code = models.IntegerField(null=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    ECG_File = models.URLField(max_length=150)
    time = models.DateTimeField(auto_now_add=True, null=True)
    # source = models.FileField(upload_to='media/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='documents/ECG12lead/', null=True, blank=True)

