from __future__ import unicode_literals
from rest_framework import serializers

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import *
from rest_framework.utils import model_meta
import string
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from beforelogin.tasks import send_password_sms, \
    send_password_email  # send_verification_email,send_restpassword_email,send_wellcom_email,send_restsussuss_email,send_wellcom_sms,send_bulkhealthtipsemail



# def Emailsendserializer(**data):
#     print "email funcion enter", data
#     mail_subject = "SUCCESSFUL REGISTRATION"
#     contentmessage = render_to_string('before_login/verification_email1', {
#         'user': data['fname'],
#         'username': data['email'],
#          'userpassword': data['password'],
#     })
#     send_password_email.apply_async(kwargs={'subject': mail_subject, 'contentmessage': contentmessage,
#                                              'sender': 'mailauthentication@cygengroup.com',
#                                              'reciver': [data['email'], ]}, queue='passwordemail')
#     send_password_sms.apply_async(kwargs={
#          'subject': 'Dear {0} Thank you for registering with LAMJINGBA HMS Your Username is {1} This Username can not be changed Your password for LAMJINGBA HMS is {2} (password change is mandatory upon first login)'.format(
#              data['fname'], data['email'], data['password']),
#          'mobilenumber': data['phone']},

#                                     queue='passwordsms')
#      # print "sms sent"
#     return "success"
class Customserializer(ModelSerializer):

    def create_nestedseriliazer(self, user_data, pro_data, validated_data):
        data = {}
        usr = userserializer.create(userserializer(), validated_data=user_data)
        password = usr.password
        usr.password = make_password(password)
        email = usr.email

        usr.save()
        if pro_data:
            pro = profileserializer.create(profileserializer(), validated_data=pro_data)
            pro.user_id = usr.id
            pro.save()
        data['email'] = email
        data['password'] = password
        # data['email'] = validated_data['email']
        # print "kkkk", email, password
        phone_1 = validated_data['phone']
        phone_2 = phone_1.split(' ')
        data['phone'] = phone_2[1]
        data['fname'] = validated_data['first_name']

        # if Emailsendserializer(**data):
        #     print "emailsend"
        user_type = validated_data['user_type']
        print user_type.id

        if pro_data:
            for i in pro_data:
                validated_data.pop(i)
            print validated_data
            if user_type.id in [2,3,5]:
                custom_update, created = Staff.objects.update_or_create(staff=usr, pro=pro, **validated_data)
            if user_type.id == 4:
                custom_update, created = Patient.objects.update_or_create(pat=usr, pro=pro, **validated_data)

            if user_type.id == 6:
                custom_update, created = CorporateHR.objects.update_or_create(hr=usr, pro=pro, **validated_data)
            # elif user_type.id == 1:
            #     custom_update, created = User.objects.update_or_create(pharma_user=usr, pro=pro, **validated_data)
            # elif user_type.id == 5:
            #     custom_update, created = Nurse.objects.update_or_create(nurse_user=usr, pro=pro, **validated_data)
            # elif user_type.id == 6:
            #     custom_update, created = Doctors.objects.update_or_create(doc=usr, pro=pro, **validated_data)
            # elif user_type.id == 7:
            #     custom_update, created = Patient.objects.update_or_create(pat=pro, **validated_data)
        else:
            custom_update, created = Profile.objects.update_or_create(user=usr, **validated_data)
        custom_update.save()
        return custom_update

    def update(self, instance, validated_data):
        # print "dess", instance.username
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                # print field
                field.set(value)
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance


class userserializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email",)

    def create(self, validated_data):
        password = BaseUserManager().make_random_password(8, string.ascii_letters + string.digits)
        validated_data['password'] = password
        print password

        return User.objects.create(**validated_data)
    def get_password(self):
        print self.pswd
        return "llkllll"

    def update(self, instance, validated_data):
        print "dess", instance.email
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                # print field
                field.set(value)
            else:
                setattr(instance, attr, value)

        instance.save()

        return instance



class profileserializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "gender", "first_name", "middle_name", "last_name", "Qualification", "user_type", "phone",)

class orgserializer(ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'

class branchserializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class corporate_branchserializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate
        fields = '__all__'

class staffserializer(ModelSerializer):
    staff = userserializer(required=True)
    pro = profileserializer(required=True)
    org_id = orgserializer(read_only=True)
    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('staff')
        pro_data = validated_data.pop('pro')
        print validated_data
        validated_data.update(pro_data)
        print "ds",validated_data
        usertype = validated_data["user_type"]
        print usertype.id
        if usertype.id in [2,3,5]:
            object = Customserializer.create_nestedseriliazer(Customserializer(), user_data=user_data, pro_data=pro_data,
                                                          validated_data=validated_data)
            return object
        else:
            raise AssertionError('usertype not matched')
    def update(self, instance, validated_data):

        print validated_data

        user_data = validated_data.pop('staff')
        pro_data = validated_data.pop('pro')
        docproobject = Customserializer.update(Customserializer(),instance=instance.pro, validated_data=pro_data)
        docusrobject = Customserializer.update(Customserializer(),instance=instance, validated_data=validated_data)
        return instance
class DoctoreditSerializer(ModelSerializer):
    doc = userserializer(read_only=True)
    pro = profileserializer(required=True)

    class Meta:
        model = Staff
        fields = "__all__"

    def update(self, instance, validated_data):

        print validated_data

        # user_data = validated_data.pop('staff')
        pro_data = validated_data.pop('pro')
        docproobject = Customserializer.update(Customserializer(),instance=instance.pro, validated_data=pro_data)
        docusrobject = Customserializer.update(Customserializer(),instance=instance, validated_data=validated_data)
        return instance

class CorphreditSerializer(ModelSerializer):
    hr = userserializer(read_only=True)
    pro = profileserializer(required=True)

    class Meta:
        model = CorporateHR
        fields = "__all__"

    def update(self, instance, validated_data):
        print validated_data

        # user_data = validated_data.pop('staff')
        pro_data = validated_data.pop('pro')
        hrproobject = Customserializer.update(Customserializer(), instance=instance.pro, validated_data=pro_data)
        hrobject = Customserializer.update(Customserializer(), instance=instance, validated_data=validated_data)
        return instance


class adminserializer(ModelSerializer):
    user = userserializer(required=True)
    class Meta:
        model = Profile
        fields = ("id","user", "gender", "first_name", "middle_name", "last_name", "user_type", "phone",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        usertype  = validated_data["user_type"]
        print usertype.id
        if usertype.id == 1:
            print validated_data
            object = Customserializer.create_nestedseriliazer(Customserializer(), user_data=user_data, pro_data=None,validated_data=validated_data)
            return object
        else:
            raise AssertionError('admin usertype not matched')

class patientserializer(ModelSerializer):
    pat = userserializer(required=True)
    pro = profileserializer(required=True)

    class Meta:
        model = Patient
        fields = '__all__'
        # exclude = "created_by",)(

    def create(self,  validated_data):
        user_data = validated_data.pop('pat')
        pro_data = validated_data.pop('pro')
	a=Usertypes.objects.get(Role_id=4)
        pro_data.update({"user_type":a})
        validated_data.update(pro_data)
        print "ds", validated_data
        usertype = validated_data["user_type"]
        print usertype.id
        if usertype.id == 4:
            object = Customserializer.create_nestedseriliazer(Customserializer(), user_data=user_data,
                                                              pro_data=pro_data,
                                                              validated_data=validated_data)
            return object
        else:
            raise AssertionError('usertype not matched')


class corphrserializer(ModelSerializer):
    hr = userserializer(required=True)
    pro = profileserializer(required=True)

    class Meta:
        model = CorporateHR
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('hr')
        pro_data = validated_data.pop('pro')
        print validated_data
        validated_data.update(pro_data)
        print "ds", validated_data
        usertype = validated_data["user_type"]
        print usertype.id
        if usertype.id == 6:
            object = Customserializer.create_nestedseriliazer(Customserializer(), user_data=user_data,
                                                              pro_data=pro_data,
                                                              validated_data=validated_data)
            return object
        else:
            raise AssertionError('usertype not matched')



class Patientlinkserializer(ModelSerializer):
    # doc_link = profileserializer(required=True)
    class Meta:
        model = Patient
        fields = ('doctorid',)

    def update(self, instance, validated_data):

        lis = instance.doctorid.all()
        print "sedse",lis
        for i in lis:
            if i in validated_data["doctorid"]:
                continue
            else:
                validated_data['doctorid'].append(i)

        info = model_meta.get_field_info(instance)
        print validated_data

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        # print validated_data
        return instance


        # return instance


class getpatientserializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        # exclude = "created_by",)(
class getphysiciannurse(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


