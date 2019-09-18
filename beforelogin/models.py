from __future__ import unicode_literals
from uuid import uuid4
from django.db import IntegrityError
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,UserManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randint
from django.utils import timezone

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     """User model."""
#
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     first_name=models.CharField(max_length=300, null=True)
#     middle_name=models.CharField(max_length=300, null=True)
#     last_name=models.CharField(max_length=300, null=True)
#     patient_code=models.IntegerField( null=True)
#     phone = models.CharField(max_length=30)
#     gender = models.CharField(max_length=30, null=True)
#     is_verified=models.BooleanField(default=False)
#     is_reset = models.BooleanField(default=True)
#     reset_time = models.DateTimeField(default=timezone.now)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = UserManager()
#
#     class Meta:
#         index_together = [
#             ("email", "phone"),
#         ]
#
#
#
# class verifcation(models.Model):
#     user = models.ForeignKey(User)
#     sluged = models.CharField(max_length=40)
#
#     def save(self, *args, **kwargs):
#         # a=self.sluged
#         if self.sluged:
#             super(verifcation, self).save(*args, **kwargs)
#             return
#
#
#         self.sluged = randint(99999, 999999)
# 	super(verifcation, self).save(*args, **kwargs)


class Usertypes(models.Model):
    stafftypes = [
        (1, _("Admin")),
        (2, _("Nursing Staff")),
        (3, _("Physician")),
        (4, _("Patient")),
        (5,_("Medtech")),
        (6, _("Corporate HR")),

    ]
    Role_id = models.PositiveSmallIntegerField(choices=stafftypes )

    def __unicode__(self):
        return '%s' % self.get_Role_id_display()


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(_('email address'),unique=True)
    password = models.CharField(_('password'), max_length=128)
    is_reset = models.BooleanField(default=True)
    #user_type = models.ForeignKey(Usertypes, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

