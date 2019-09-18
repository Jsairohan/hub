# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from serializers import *
from usermanagement.models import *
from django.contrib.auth.hashers import make_password
from healthandrecords.models import evaluation_form, Risk_sore
from apiforapp.models import Ecgmeter
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from beforelogin.models import User
from healthandrecords.cardiac_risk_scores import *
from healthandrecords.diabetes_risk_score import *
from healthandrecords.calculators import Claries, Bmr, Bfp
from django.forms.models import model_to_dict
from foodandacti.models import Userinfosummary
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
import random
from beforelogin.models import *
import string
from beforelogin.tasks import send_verification_email, send_restpassword_email, send_wellcom_email, \
    send_restsussuss_email, send_wellcom_sms, send_bulkhealthtipsemail, send_password_email, send_password_sms
from django.template.loader import render_to_string
from healthandrecords.models import CheckParams
from foodandacti.summriskpre import *
from apiforapp.riskupdater import updaterisk
import os
from django.views.static import serve
from django.conf import settings
from rest_framework import views
from usermanagement.models import Patient
from apiforapp.riskapformb import *


# random.choice(foo)
# Create your views here.
# {'patient_code': 133333332, 'first_name': 'New', 'password': 'cygen@123', 'email': 'test2344444444444@test.com'}

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


mandatotry_field_list = ["smoker", "employment", "anualincome", "family_diabetes", "hypertension",
                         "waist_circumference",
                         "exercise", "geostational_diabetes", "treated_for_systolic_bp", "gender", "ethnicity"]


def if_mandatotry_fields_exists(jsonobj):
    missed_field = None
    if missed_field is None:
        for field in mandatotry_field_list:
            if jsonobj.get(field) is not None:
                pass
            else:

                missed_field = field
    return missed_field


class Createpatientview(APIView):
    def post(self, request, format=None):
        validated_data = request.data
        obj = User.objects.filter(email=validated_data.get("email")) or User.objects.filter(
            patient_code=validated_data.get("patient_code"))
        # print obj 222221
        if obj:
            obj = obj[0]
        if validated_data.get("patient_code"):
            pass
        else:
            validated_data["patient_code"] = None
        name = validated_data["name"]
        splitname = name.split(':')
        validated_data["first_name"] = splitname[0]
        validated_data["middle_name"] = splitname[1]
        validated_data["last_name"] = splitname[2]
        validated_data.pop('name')
        # validated_data[""] =
        print validated_data
        # for key, value in validated_data.items():
        #   print key, value

        password = BaseUserManager().make_random_password(8, string.ascii_letters + string.digits)
        validated_data['password'] = password
        rpass = validated_data['password']
        print rpass, 'sjhfkjhkjh'
        if not obj:
            a = User.objects.create(email=validated_data.get("email"), patient_code=validated_data.get("patient_code"),
                                    first_name=validated_data.get("first_name"),
                                    middle_name=validated_data.get("middle_name"),
                                    last_name=validated_data.get("last_name"), gender=validated_data.get("gender"),
                                    is_verified=True,
                                    phone=validated_data.get("phno"), password=make_password(rpass))
            a.save()
            print a.email, 'kjafskjh'
            print a.phone, 'ahdskjhaskj'
            print rpass, 'random'

            mail_subject = "SUCCESSFUL REGISTRATION"
            contentmessage = render_to_string('before_login/verification_email1', {
                'user': a.first_name,
                'email': a.email,
                'userpassword': rpass,
            })
            send_password_email.apply_async(kwargs={'subject': mail_subject, 'contentmessage': contentmessage,
                                                    'sender': 'mailauthentication@cygengroup.com',
                                                    'reciver': [a.email, ]}, queue='passwordemail')

            # send_password_sms.apply_async(kwargs={'subject': 'Dear {0} Thank you for registering with Aimhealth Your email is {1} and Your password for Aimhealth is {2}'.format(a.first_name, a.email, rpass),'mobilenumber': a.phone},queue='passwordsms')
            print("sms sent")
            print("success")

            return Response({"Success": "User created"}, status=status.HTTP_201_CREATED)



        elif obj and not obj.patient_code:
            obj.patient_code = validated_data.get("patient_code")
            obj.save()
            print obj, "obj and  not obj.patient_code"
            return Response({"Success": "User created"}, status=status.HTTP_201_CREATED)
        elif obj and obj.patient_code:
            return Response({"error": "code and email already taken"}, status=status.HTTP_400_BAD_REQUEST)

        # if not obj:
        #     a = User.objects.create(email=validated_data.get("email"), patient_code=validated_data.get("patient_code"),
        #                             first_name=validated_data.get("first_name"), is_verified=True,
        #                             phone=validated_data.get("phno"), password=make_password("cygen@123"))
        #     return Response({"Success": "User created"}, status=status.HTTP_201_CREATED)
        # elif obj and not obj.patient_code:
        #     obj.patient_code = validated_data.get("patient_code")
        #     obj.save()
        #     print obj, "obj and  not obj.patient_code"
        #     return Response({"Success": "User created"}, status=status.HTTP_201_CREATED)
        # elif obj and obj.patient_code:
        #     return Response({"error": "code and email already taken"}, status=status.HTTP_400_BAD_REQUEST)


def evaluationview_details(request):
    # data=request.data

    id = request.data.get("patient_code")
    print id
    # risk_obj = Risk_sore()
    user = Patient.objects.filter(patient_code=id).last()
    print request.data.get("patient_code"), user
    if user:
        any_field_missing = if_mandatotry_fields_exists(request.data)
        if any_field_missing is None:

            request.data["user"] = user.pat_id

            request.data["smoker"] = request.data.get("smoker").capitalize()
            request.data["employment"] = request.data.get("employment").capitalize()
            request.data["anualincome"] = request.data.get("anualincome")
            request.data["family_diabetes"] = request.data.get("family_diabetes").capitalize()
            request.data["hypertension"] = request.data.get("hypertension").capitalize()
            request.data["waist_circumference"] = request.data.get("waist_circumference")
            request.data["exercise"] = request.data.get("exercise").capitalize()
            request.data["geostational_diabetes"] = request.data.get("geostational_diabetes").capitalize()
            request.data["treated_for_systolic_bp"] = request.data.get("treated_for_systolic_bp").capitalize()
            request.data["gender"] = request.data.get("gender").capitalize()
            request.data["ethnicity"] = request.data.get("ethnicity").capitalize()
            del request.data["hdl_level"]
            del request.data["total_cholestoral"]
            h1 = int(request.data.get("h_feet"))
            h2 = int(request.data.get("h_inches"))
            height_in_inches = (((h1 * 12) + (h2)))
            height_in_cm = (height_in_inches) * (2.54)
            height_in_meters = ((height_in_inches) * (0.0254)) ** 2

            height_in_meters = ((float((height_in_inches) * (0.0254))) ** 2)
            bmi = float(float(request.data.get("weight")) / (height_in_meters))
            bmrmy = Bmr()
            bmrmy.age = int(request.data.get("age"))
            bmrmy.weight = int(request.data.get("weight"))
            bmrmy.height = int(height_in_cm)

            bmrmy.gender = request.data.get("gender").capitalize()
            if request.data.get("gender") == 'Male':
                b = bmrmy.men_bmr()
            else:
                b = bmrmy.women_bmr()
            request.data["bmr"] = b
            return "no missing fields", request.data
        else:
            return "missing fields", any_field_missing

    else:

        return None, None


class Createpatientevaluvationview(generics.CreateAPIView):
    serializer_class = Patientevaluvationserializer

    def create(self, request, *args, **kwargs):
        print request.data
        a = evaluationview_details(request)
        print a, "sample response"
        if a[0] is None:
            return JsonResponse({
                "patient code not in use": "use the url and register first https://www.cygen.in/registration/ to countioue "},
                status=400)
        elif a[0] == "missing fields":
            return Response({"field missing": a[1]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=a[1])
            serializer.is_valid(raise_exception=True)
            print "serailizer is valid "

            self.perform_create(serializer)
            print "serailizer perform created "
            headers = self.get_success_headers(serializer.data)
            print "headers are sucessful"
            # responedata={"Evaluvation parameters":serializer.data,"risk scores":b}
            # print headers
            print "about to complete evaluation "
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Getpatientevaluvationview(generics.RetrieveAPIView):
    lookup_field = 'user_id'
    queryset = evaluation_form.objects.all()
    serializer_class = Patientevaluvationserializer
    lookup_url_kwarg = 'patient_code'

    def getuserid(self):
        filter_kwargs = {'patient_code': self.kwargs[self.lookup_url_kwarg]}
        # print filter_kwargs,'djdjdjdjdjdjdjddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
        return get_object_or_404(User, **filter_kwargs)

    def get_object(self):
        from django.shortcuts import get_object_or_404

        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )
        jrobj = self.getuserid()

        if jrobj:
            filter_kwargs = {self.lookup_field: jrobj.id}
            obj = queryset.filter(**filter_kwargs).last()
            if obj:

                # May raise a permission denied
                self.check_object_permissions(self.request, obj)

                return obj
            else:
                raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
        return jrobj

class Getpatienteriskscoreview(generics.RetrieveAPIView):
    lookup_field = 'user_id'
    queryset = Risk_sore.objects.all()
    serializer_class = Patientriskserializer
    lookup_url_kwarg = 'patient_code'

    def getuserid(self):
        filter_kwargs = {'patient_code': self.kwargs[self.lookup_url_kwarg]}
        return get_object_or_404(Patient, **filter_kwargs)

    def get_object(self):
        from django.shortcuts import get_object_or_404

        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )
        jrobj = self.getuserid()

        if jrobj:
            filter_kwargs = {self.lookup_field: jrobj.pat_id}
            obj = queryset.filter(**filter_kwargs).last()
            if obj:

                # May raise a permission denied
                self.check_object_permissions(self.request, obj)

                return obj
            else:
                raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
        return jrobj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance)

        check = CheckParams.objects.filter(user=serializer.data['user']).last()

        user = User.objects.filter(id=serializer.data['user']).last()
        pat = Patient.objects.get(pat_id =serializer.data['user'])
        gen = (pat.pro.gender).title()
        d = serializer.data
        color_dict = {"Low": "#00cc00", "Normal": "#00cc00", "Moderate": "#e6e600", "High": "#ff3333",
                      "Overweight": "#e6e600",
                      "Pre-Obese": "#e6e600", "Underweight": "#ff3333", "Obese": "#ff3333", "Diagnosed": "#000000",
                      None: "#000000"
                      }
        if (check is not None) and (user is not None):
            dic = {}
            dic['heart_score'] = d["heart_score"]
            heart = heartdiaplay(d["heart_score"], gen)
            d["heart_score"] = cardiacapi(gen, dic, check.heart_score_param, color_dict[heart[0]], heart[0])
            dic.pop('heart_score')
            dic["diabetes_score"] = d["diabetes_score"]
            diabet = diabdiaplay(d["diabetes_score"])
            che = check.diabetes_param
            d["diabetes_score"] = dabetiesapi(gen, dic, che, color_dict[diabet[0]], diabet[0])
            dic.pop('diabetes_score')
            dic["hyper_score"] = d["hyper_score"]
            hypers = hyperdiaplay(d["hyper_score"])
            che = check.hyper_score_param
            d["hyper_score"] = hyperapi(gen, dic, che, color_dict[hypers[0]], hypers[0])

            del d["h_per"]
            if check.obesity == "yes":
                d["obesity"] = {"val": 50, "text": "Diagnosed", "color": "black", "max": 50, "min": 10}
            else:
                if d["bmi"] == 0:
                    d["obesity"] = {"val": "None", "text": "weight", "color": "black", "max": 50, "min": 10}
                else:
                    d["obesity"] = {"val": str(d["bmi"]), "text": check.obesity, "color": color_dict[check.obesity],
                                    "max": 50, "min": 10}
        else:
            desd = serializer.data
            for i in d:
                if i not in ("score_id", "user"):
                    desd[i] = "no data"
            return Response(desd)

        return Response(d)

class Getpatientriskview(generics.RetrieveAPIView):
    lookup_field = 'user_id'
    queryset = Risk_sore.objects.all()
    serializer_class = Patientriskserializer
    lookup_url_kwarg = 'patient_code'

    def getuserid(self):
        filter_kwargs = {'patient_code': self.kwargs[self.lookup_url_kwarg]}
        # print filter_kwargs,'djdjdjdjdjdjdjddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
        return get_object_or_404(User, **filter_kwargs)

    def get_object(self):
        from django.shortcuts import get_object_or_404

        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())
        print queryset
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )
        jrobj = self.getuserid()

        if jrobj:
            filter_kwargs = {self.lookup_field: jrobj.id}
            obj = queryset.filter(**filter_kwargs).last()
            if obj:

                # May raise a permission denied
                self.check_object_permissions(self.request, obj)

                return obj
            else:
                raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
        return jrobj


class Createpatientinformationview(generics.CreateAPIView):
    serializer_class = Patientuserinfoserializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(patient_code=request.data["patient_code"])
        somedetails = evaluation_form.objects.filter(user_id=user.id).last()
        request.data["user"] = user.id
        request.data["MaritalStatus"] = somedetails.maritial_status
        request.data["name"] = user.first_name
        request.data["PhoneNo"] = user.phone
        request.data["email"] = user.email
        request.data["age"] = somedetails.age
        request.data["Gender"] = somedetails.gender
        request.data["EmployedStatus"] = somedetails.employment
        request.data["HousingStatus"] = somedetails.housing_status

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Getpatientinformationview(generics.RetrieveAPIView):
    lookup_field = 'user_id'
    queryset = Userinfosummary.objects.all()
    serializer_class = Patientuserinfoserializer
    lookup_url_kwarg = 'patient_code'

    def getuserid(self):
        filter_kwargs = {'patient_code': self.kwargs[self.lookup_url_kwarg]}
        # print filter_kwargs,'djdjdjdjdjdjdjddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
        return get_object_or_404(User, **filter_kwargs)

    def get_object(self):
        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        jrobj = self.getuserid()

        if jrobj:
            filter_kwargs = {self.lookup_field: jrobj.id}

            obj = get_object_or_404(queryset, **filter_kwargs)

            # May raise a permission denied
            self.check_object_permissions(self.request, obj)

            return obj
        return jrobj


def ifuser_details(request):
    # data=request.data

    id = request.data.get("patient_code")
    # risk_obj = Risk_sore()
    us = Patient.objects.get(patient_code=id)
    print us.pat.id
    user = User.objects.filter(id=us.pat_id).last()
    if user:

        return request.data
    else:

        return None


class Createglucosview(generics.CreateAPIView):
    serializer_class = glucosserializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data.pop("type")
        a = ifuser_details(request)
        if not a:
            return JsonResponse({
                "patient code not in use": "use the url and register first https://www.cygen.in/registration/ to countioue "},
                status=400)
        else:

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Createoximeterview(generics.CreateAPIView):
    serializer_class = oximeterserializer

    def create(self, request, *args, **kwargs):
        request.data["spo"] = request.data.get("spo2")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Createhdlmeterview(generics.CreateAPIView):
    serializer_class = Hdlmmeterserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CreateTemperatureview(generics.CreateAPIView):
    serializer_class = Temperatureserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CreateBpmmeterview(generics.CreateAPIView):
    serializer_class = Bpmmeterserializer

    def create(self, request, *args, **kwargs):
        a = ifuser_details(request)
        if not a:
            return JsonResponse({
                "patient code not in use": "use the url and register first https://www.cygen.in/registration/ to countioue "},
                status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CreateWeightmeterview(generics.CreateAPIView):
    serializer_class = Weightmeterserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CreateSpirometeryview(generics.CreateAPIView):
    serializer_class = Spirometeryserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Himobloginpostview(generics.CreateAPIView):
    serializer_class = Himobloginmeterserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Hbacpostview(generics.CreateAPIView):
    serializer_class = Hbacmeterserializer

    def create(self, request, *args, **kwargs):
        if request.data.get("hba1c"):
            request.data["hbac"] = request.data.get("hba1c")
        print request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Ldlpostview(generics.CreateAPIView):
    serializer_class = Ldlmeterserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class Hdlpostview(generics.CreateAPIView):
#     serializer_class = Spirometeryserializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Totalcolestrolpostview(generics.CreateAPIView):
    serializer_class = Totalcolestrolmeterserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Triglecyridespostview(generics.CreateAPIView):
    serializer_class = Triglecyridesmeterserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Urinepostview(generics.CreateAPIView):
    serializer_class = Urinemetermeterserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Evaluationcreateview(generics.CreateAPIView):
    serializer_class = Evaluationserializer


class ECGcreateview(generics.CreateAPIView):
    serializer_class = ECGserializer


class paramcreateview(generics.ListAPIView):
    lookup_field = 'id'
    queryset = CheckParams.objects.all()
    serializer_class = Checkserializer


class ECGgetview(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Ecgmeter.objects.all()
    serializer_class = ECGserializer


class ECGNIGcreateview(generics.CreateAPIView):
    serializer_class = ECGNigserializer


class Evaluationgetview(generics.ListAPIView):
    lookup_field = 'id'
    queryset = evaluation_form.objects.all()
    serializer_class = Evaluationserializer


def openfle(request, path):
    filepath = settings.BASE_DIR
    path = os.path.abspath(path)
    filepath = os.path.join(filepath, path)
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def buhn(request):
    dic = {
        "id": 228,
        "age": "23",
        "weight": 40.0,
        "h_feet": 5,
        "h_inches": 3,
        "gender": "Male",
        "smoker": "Yes",
        "bp_systolic": None,
        "bp_diastolic": "85",
        "employment": "Self Employed",
        "anualincome": "500000",
        "maritial_status": "Single",
        "housing_status": "Rent",
        "drinker": None,
        "cardiac": "Yes",
        "obesity": "no",
        "health_condition": None,
        "eat_vegetables": None,
        "hospital_screening": None,
        "family_diabetes": None,
        "ethnicity": "Asian",
        "hypertension": None,
        "waist_circumference": None,
        "diabetes": "No",
        "exercise": "little_exercise",
        "geostational_diabetes": None,
        "treated_for_systolic_bp": "Yes",
        "hdl_level": "20.0",
        "total_cholestoral": "230.0",
        "blood_glucose": None,
        "bmr": 1290.125,
        "user": 313,
    }
    dds = {
        "id": 338,
        "age": "42",
        "weight": 83.7,
        "h_feet": 5,
        "h_inches": 7,
        "gender": "Male",
        "smoker": "No",
        "bp_systolic": "129.0",
        "bp_diastolic": "77.0",
        "employment": "Employed",
        "anualincome": "225120",
        "maritial_status": "Single",
        "housing_status": "Rent",
        "drinker": "yes",
        "health_condition": "no",
        "eat_vegetables": "yes",
        "hospital_screening": "no",
        "family_diabetes": "No",
        "ethnicity": "Asian",
        "hypertension": "Yes",
        "waist_circumference": "94",
        "diabetes": "no",
        "exercise": "Yes",
        "geostational_diabetes": "No",
        "treated_for_systolic_bp": "No",
        "hdl_level": "64.0",
        "total_cholestoral": "240.0",
        "blood_glucose": "0",
        "bmr": 1667.5,
        "user": 313,
        "cardiac": "Yes",
        "obesity": "no",
    }
    o = CheckParams()
    print "sddssd"
    ds = updaterisk(dds)
    return HttpResponse("<h1>{}</h1>".format(ds))
