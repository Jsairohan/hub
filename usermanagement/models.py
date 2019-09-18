from __future__ import unicode_literals
from uuid import uuid4
from django.db import IntegrityError
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randint
from django.utils import timezone
from beforelogin.models import User,Usertypes


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=False, unique=False, null=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    middle_name = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    user_type = models.ForeignKey(Usertypes, on_delete=models.SET_NULL, null=True)
    reset_time = models.DateTimeField(default=timezone.now)
    Qualification = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Distributor(models.Model):
    organization_name = models.CharField(max_length=100, null=True)
    organization_id = models.CharField(max_length=10, null=True, unique=True)
    organization_address = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.organization_name


class Branch(models.Model):
    organaisation_code = models.ForeignKey(Distributor, null=True)
    branch_name = models.CharField(max_length=100, null=True)
    branch_code = models.SlugField(editable=False, )
    branch_address = models.CharField(max_length=500, null=True)

    def save(self, *args, **kwargs):
        if not self.branch_code:
            org_var = self.organaisation_code.organization_id.upper()
            # a=Branch_id.objects.all()
            # for i in a:
            #     for j in i:
            #         print j
            count = Branch.objects.filter(branch_code__startswith=org_var).count() + 1
            count + 1
            self.branch_code = "{}-{:02d}".format(org_var, count)
            print self.branch_code
        super(Branch, self).save(*args, **kwargs)


class Corporate(models.Model):
    corporate_name = models.CharField(max_length=100, null=True)
    corporate_code = models.CharField(max_length=10, unique=True)
    corporate_branch_address = models.CharField(max_length=500, null=True)
    number_of_visits = models.CharField(max_length=100, null=True)


# @receiver(post_save,sender = organizationid)
# def slots(sender, instance, **kwargs):
#     org = instance.organization_id
#     org_id = staff.objects.create(choices=org)
#     org_id.save()
#     print org_id

class Staff(models.Model):
    pro = models.OneToOneField(Profile, primary_key=False, null=True)
    staff = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    branch_code = models.CharField(max_length=100, null=True)
    speciality = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Licence_number = models.CharField(max_length=100)


class Patient(models.Model):
    PHID = models.SlugField(editable=False,null=True )

    phillhealth_id=models.TextField(null=True)
    branch_code = models.CharField(null=True,max_length=100)
    employee_id=models.TextField(null=True)
    patient_type=models.CharField(null=True,max_length=100)
    corporate_code = models.CharField(null=True,max_length=100)

    pat = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pro = models.OneToOneField(Profile, primary_key=False, null=True)
    patient_code = models.IntegerField(null=True,unique=True)
    # corporate = models.ForeignKey(Corporate, on_delete=models.CASCADE, null=True)
    doctorid = models.ManyToManyField(Staff, null=True, blank=True)
    # created_by = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        if not self.PHID:
            if self.phillhealth_id != None :
                print self.branch_code
                print self.phillhealth_id

                self.PHID=(self.branch_code)+'-'+self.phillhealth_id
                print self.PHID
            else:
                count = Patient.objects.all().count() + 1
                count + 1
                a=self.branch_code

                self.PHID = "{}-{}{:09d}".format(a,'NPH', count)
                print self.PHID
        super(Patient, self).save(*args, **kwargs)


class CorporateHR(models.Model):
    hr = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pro = models.OneToOneField(Profile, primary_key=False, null=True)
    # emp_id = models.CharField(max_length=300)
    branch_code = models.CharField(max_length=100, null=True)
    employee_code = models.CharField(max_length=100, null=True)
    Designation = models.CharField(max_length=100, null=True)
    branch_name = models.CharField(max_length=100, null=True)



class Treatment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE,null =True)
    patient = models.IntegerField(null =True)
    istreated = models.BooleanField(default=False)

