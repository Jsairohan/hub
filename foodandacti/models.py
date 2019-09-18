# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date,datetime
from uuid import uuid4
from django.db import IntegrityError
from django.urls import reverse
from beforelogin.models import User
# Create your models here.
class setgoalsd(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL, null=True,blank=True)
    targetnumberkg=models.IntegerField()
    targetdays=models.IntegerField()
    change_type=models.CharField(max_length=50,null=True)
    calneeded=models.FloatField(null=True)
    editeedon=models.DateField(default=date.today,null=True)

class activitysecduled(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    dayofweek=models.CharField(max_length=50)
    exercise=models.CharField(max_length=50)
    howtime=models.IntegerField()
    calburnt=models.FloatField()
    createdDate = models.DateTimeField(default=datetime.now())
    isperformed=models.CharField(max_length=50,default="", null=True)



class Medicationlogs(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    PrescriptionDate = models.CharField(max_length=300, null=True)
    MedicationName = models.CharField(max_length=300, null=True)
    # CompositionName = models.CharField(max_length=300, null=True)
    Doctor = models.CharField(max_length=300, null=True)
    Dosage = models.CharField(max_length=300, null=True)
    TimesPerDay = models.CharField(max_length=300, null=True)
    WithFood = models.CharField(max_length=300, null=True)
    Reason = models.CharField(max_length=300, null=True)
    Reactions = models.CharField(max_length=300, null=True)
    timmings = models.CharField(max_length=300, null=True)
    TMR_of_medicine = models.CharField(max_length=300, null=True)
    HWT_of_medicine = models.CharField(max_length=300, null=True)



# class Medicationlog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     PrescriptionDate = models.CharField(max_length=300, null=True)
#     MedicationName = models.CharField(max_length=300, null=True)
#     Doctor = models.CharField(max_length=300, null=True)
#     Dosage = models.CharField(max_length=300, null=True)
#     TimesPerDay = models.CharField(max_length=300, null=True)
#     WithFood = models.CharField(max_length=300, null=True)
#     Reason = models.CharField(max_length=300, null=True)
#     Reactions = models.CharField(max_length=300, null=True)

class Doctorpresciption(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    docname = models.CharField(max_length=300, null=True)
    prescription = models.TextField(null=True)
    patient = models.CharField(max_length=300, null=True)
    createdDate = models.CharField(max_length=50,null=True)

class DoctorTherepaticpresciption(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    docname_t = models.CharField(max_length=300, null=True)
    prescription_t = models.TextField(null=True)
    patient_t = models.CharField(max_length=300, null=True)
    createdDate_t = models.CharField(max_length=50,null=True)

class Userinfosummary(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    PhoneNo = models.CharField(max_length=50)
    age = models.IntegerField()
    Gender = models.CharField(max_length=50)
    Address = models.CharField(max_length=250)
    hospitalAddress = models.CharField(max_length=250)
    guardianname = models.CharField(max_length=50)
    ContactNo = models.CharField(max_length=50)
    gAddress = models.CharField(max_length=250)
    Doctorname = models.CharField(max_length=50)
    Doctornumb = models.CharField(max_length=50)
    MaritalStatus = models.CharField(max_length=50)
    EmployedStatus = models.CharField(max_length=50)
    HousingStatus = models.CharField(max_length=50)
    allergy =models.CharField(max_length=250)




class Foodsecd(models.Model):
    uid=models.IntegerField( null=True)
    breakf=models.CharField(max_length=300,null=True)
    lunch=models.CharField(max_length=300,null=True)
    dinner=models.CharField(max_length=300,null=True)
    secuded=models.DateField(null=True)
    cal_food=models.CharField(max_length=30, null=True)
    ver_son=models.CharField(max_length=30, null=True)
    exerc=models.CharField(max_length=150, null=True)
    durations=models.CharField(max_length=15, null=True)
    editeedon=models.DateField(auto_now=True,null=True)


class Food_details(models.Model):
    Serving_Size=models.CharField(max_length=300,null=True)
    Calories=models.CharField(max_length=300,null=True)
    Fat=models.CharField(max_length=300,null=True)
    Carbs=models.CharField(max_length=300,null=True)
    Protein=models.CharField(max_length=300,null=True)
    fodd_name=models.CharField(max_length=300,null=True)


class usersfoodsdairy(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    sluged = models.CharField(max_length=40, unique=True)
    Calories=models.CharField(max_length=50,null=True)
    Fat=models.CharField(max_length=50,null=True)
    Carbs=models.CharField(max_length=50,null=True)
    Protein=models.CharField(max_length=50,null=True)
    fodd_name=models.CharField(max_length=100,null=True)
    wheninday=models.CharField(max_length=50,null=True)
    fooddate=models.DateField(null=True)
    editeedon=models.DateField(auto_now=True,null=True)
    isconsumed=models.CharField(max_length=50,default="", null=True)
    def save(self, *args, **kwargs):
        if self.sluged:
            super(usersfoodsdairy, self).save(*args, **kwargs)

        unique = False
        while not unique:
            try:
                self.sluged = uuid4().hex
                super(usersfoodsdairy, self).save(*args, **kwargs)
            except IntegrityError:
                self.sluged = uuid4().hex
            else:
                unique = True

    def get_absolute_url(self):
        return reverse('food:editss', kwargs={'slug': self.sluged})


#http://www.nutristrategy.com/activitylist4.htm

class fit_ex(models.Model):
    activity=models.CharField(max_length=300,null=True)
    kg_41=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_45=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_50=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_54=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_59=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_64=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_68=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_73=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_77=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_82=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_86=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_91=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_100=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_109=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_118=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_127=models.DecimalField(max_digits=6, decimal_places=2,null=True)
    kg_136=models.DecimalField(max_digits=6, decimal_places=2,null=True)



class transfor(models.Model):
  weight_gain=models.IntegerField(null=True)
  gain_time=models.IntegerField(null=True)
  activity=models.IntegerField(null=True)
  activityname=models.CharField(max_length=300,null=True)
  act_time=models.IntegerField(null=True)

  weight_loss=models.IntegerField(null=True)
  loss_time=models.IntegerField(null=True)
  typer=models.CharField(max_length=300,null=True)
  calneeded=models.IntegerField(null=True)
  date = models.DateTimeField(auto_now_add=True, blank=True)

class recipefoods(models.Model):
    foodname=models.CharField(max_length=150,null=True)
    Energy=models.FloatField()
    Protein=models.CharField(max_length=50,null=True)
    Carbohydrates=models.CharField(max_length=50,null=True)
    Fiber=models.CharField(max_length=50,null=True)
    Fat=models.CharField(max_length=50,null=True)
    Cholesterol=models.CharField(max_length=50,null=True)
    Sodium=models.CharField(max_length=50,null=True)
    Zinc=models.CharField(max_length=50,null=True)
    Potassium=models.CharField(max_length=50,null=True)
    Calcium=models.CharField(max_length=50,null=True)
    VitaminA=models.CharField(max_length=50,null=True)
    Magnesium=models.CharField(max_length=50,null=True)
    Phosphorus=models.CharField(max_length=50,null=True)
    FolicAcid=models.CharField(max_length=50,null=True)
    specifirecipe=models.CharField(max_length=50,null=True)
# class foodsecdule(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)

