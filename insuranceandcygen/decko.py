from functools import wraps

from beforelogin.models import User
from django.core.exceptions import PermissionDenied
from healthandrecords.cardiac_risk_scores import *
from healthandrecords.diabetes_risk_score import *
from healthandrecords.models import *
import collections
from beforelogin.views import Geter_cache

from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404,redirect
import requests
from healthandrecords.models import evaluation_form
from healthandrecords.calculators import Claries,Bmr,Bfp
from apiforapp.models import Bpmmeter
from usermanagement.models import *

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def dash_compleletd(function):
    def wrap(request, *args, **kwargs):
        id = request.user.id
        # cah_user = cache.get(id)
        # det = {'risk_score':'' , 'person_details': ''}
        # print id,'sfd'
        # user = User.objects.get(id=id)
        # pro = Profile.objects.get(user=user)
        # print pro.is_verified,'poooo'
        # if request.pro.is_verified:
        #     pass
        # else:
        #     return render(request, 'before_login/verificationcode.html')
        details = {}
        rs = Risk_sore.objects.filter( user_id=id).last()

        # print rs,'rrrrrrrrrrrrrrrrrrsssssssssssssssssssssss'

        details['risk_score'] = rs
        pd =evaluation_form.objects.filter(user_id=id).last()
        details['profile_details'] = pd
        rr=details['profile_details']
        # print rr.user.patient_code
        if not rr:
            c = {"context1": 'Data is incomplete.'}
            return render(request, 'navbar/newbpmeter.html', c)
        else:
            pass
        rp = Patient.objects.get(pat_id = id)
        if rr and not rs:
            if rp.patient_code :

                bpm = Bpmmeter.objects.filter(patient_code=rp.patient_code).last()

                if not bpm:
                    c={"context1":'Data is incomplete'}
                    return render(request, 'navbar/newbpmeter.html', c)


                ris_url = requests.get('http://127.0.0.1:8000/riskscore/get/' + str(rp.patient_code) + '/')

                details['risk_score'] = rs


        else:
            details['risk_score'] = rs



        risk_details = details.get('risk_score')

        if risk_details:


            return function(request, *args, **kwargs)
        else:
            return redirect( '/profile_form/')



    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

# def dash_compleletd(function):
#     def wrap(request, *args, **kwargs):
#         id = request.user.id
#         # cah_user = cache.get(id)
#         # det = {'risk_score':'' , 'person_details': ''}
#         if request.user.is_verified:
#             pass
#         else:
#             return render(request, 'before_login/verificationcode.html')
#         details = {}
#         rs = Risk_sore.objects.filter( user_id=id).last()
#
#         # print rs,'rrrrrrrrrrrrrrrrrrsssssssssssssssssssssss'
#
#         details['risk_score'] = rs
#         pd =evaluation_form.objects.filter(user_id=id).last()
#         details['profile_details'] = pd
#         rr=details['profile_details']
#         # print rr.user.patient_code
#         if not rr:
#             c = {"context1": 'Data is incomplete.'}
#             return render(request, 'navbar/newbpmeter.html', c)
#         else:
#             pass
#
#         if rr and not rs:
#             if rr.user.patient_code :
#
#                 bpm = Bpmmeter.objects.filter(patient_code=rr.user.patient_code).last()
#
#                 if not bpm:
#                     c={"context1":'Data is incomplete'}
#                     return render(request, 'navbar/newbpmeter.html', c)
#
#
#                 ris_url = requests.get('http://127.0.0.1:8000/riskscore/get/' + str(rr.user.patient_code) + '/')
#
#                 details['risk_score'] = rs
#
#
#         else:
#             details['risk_score'] = rs
#
#
#
#         risk_details = details.get('risk_score')
#
#         if risk_details:
#
#
#             return function(request, *args, **kwargs)
#         else:
#             return redirect( '/profile_form/')
#
#
#
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap

# def dash_compleletd(function):
#     def wrap(request, *args, **kwargs):
#
#         id=request.user.id
#         # cah_user = cache.get(id)
#         # det = {'risk_score':'' , 'person_details': ''}
#         if request.user.is_verified:
#             pass
#         else:
#             return render(request, 'before_login/verificationcode.html')
#         details ={}
#         rs = get_or_none(Risk_sore, user_id=id)
#
#         print rs,'risk score'
#
#         details['risk_score'] = rs
#         cache.set(id, details, 180 * 60)
#         cah_user = cache.get(id)
#
#
#         risk_details = details.get('risk_score')
#
#         if risk_details:
#
#
#             return function(request, *args, **kwargs)
#         else:
#             return redirect( '/profile_form/')
#
#
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap