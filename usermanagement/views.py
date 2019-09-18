# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect

from django.shortcuts import render
from serializers import *
from django.contrib.auth.hashers import make_password
from healthandrecords.models import evaluation_form, Risk_sore
from apiforapp.models import Ecgmeter
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from beforelogin.models import User
from .models import *
from apiforapp.models import *
from foodandacti.models import *
from foodandacti import summriskpre
from healthandrecords.cardiac_risk_scores import *
from healthandrecords.diabetes_risk_score import *
from healthandrecords.calculators import Claries, Bmr, Bfp
from django.forms.models import model_to_dict
from foodandacti.models import Userinfosummary
from apiforuser import *
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
import random
import string
from beforelogin.tasks import send_verification_email,send_restpassword_email,send_wellcom_email,send_restsussuss_email,send_wellcom_sms,send_bulkhealthtipsemail,send_password_email,send_password_sms
from django.template.loader import render_to_string
from healthandrecords.models import CheckParams
from foodandacti.summriskpre import *
from apiforapp.riskupdater import updaterisk
import os
from django.views.static import serve
from django.conf import settings
from rest_framework import views
from healthandrecords.models import evaluation_form,Risk_sore
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from foodandacti import summriskpre
from datetime import datetime
from django.utils import timezone
from django.db.models.functions import Concat
from django.db.models import Count, F, Value
#
from django.db.models import OuterRef, Subquery
from django.db.models import Max
from django.db.models.expressions import RawSQL
from django.db.models.query import QuerySet
from healthandrecords.models import *

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


class Createstaffview(CreateAPIView):
    serializer_class = staffserializer

class Createadmin(CreateAPIView):
    serializer_class = adminserializer

class Createpatient(CreateAPIView):
    serializer_class = patientserializer
    def create(self, request, *args, **kwargs):
        ass=request.data
        session_id_for=ass['session_id']
        daeerer = Staff.objects.filter(staff_id=session_id_for)[0].branch_code
        ass['branch_code'] = daeerer
        serializer = self.get_serializer(data=ass)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Createorgid(CreateAPIView):
    serializer_class = orgserializer
class getorgid(ListAPIView):
    serializer_class = orgserializer
    queryset = Distributor.objects.all()


class Createbranchid(CreateAPIView):
    serializer_class = branchserializer

class Createcorporatebranchid(CreateAPIView):
    serializer_class = corporate_branchserializer



def adminview(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    doccount = Staff.objects.filter(pro__user_type_id=3).count()
    nurcount = Staff.objects.filter(pro__user_type_id=2).count()
    medTechcount = Staff.objects.filter(pro__user_type_id=5).count()
    orgcount = Distributor.objects.all().count()
    branchcount = Branch.objects.all().count()
    corphrcount = CorporateHR.objects.filter(pro__user_type_id=6).count()
    corphbranchcount = Corporate.objects.all().count()
    context = {"doccount":doccount,"nurcount":nurcount,"medTechcount":medTechcount,"orgcount":orgcount,"branchcount":branchcount,
                "corphrcount":corphrcount,"corphbranchcount":corphbranchcount}
    if user ==1:
        admin = Profile.objects.filter(user_type_id=1).count()
        print "super"
        context["admincount"]=admin
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request,'navbar/admindashboard.html',context)

def adminlistview(request):

    return render(request,'navbar/adminpage.html')

def doctorview(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    context={}
    if user ==1:
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request,'navbar/doctor.html',context)

def nurseview(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    context={}
    if user ==1:
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request,'navbar/nurse.html',context)

def medtechview(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    context={}
    if user ==1:
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request,'navbar/medtech.html',context)

def organizationview(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    context={}
    if user ==1:
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request,'navbar/organization.html',context)

def branchview(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    context={}
    if user ==1:
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request,'navbar/branch.html',context)
def corporate_branchview(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    context={}
    if user ==1:
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request,'navbar/corporatebranch.html',context)

# def doctordashboardview(request):
#     return render(request,'navbar/doctordashboard.html')
#

def doctordashboardview(request):
    did = request.user.id
    trecount = Treatment.objects.filter(doctor=did,istreated=True) .count()
    untrecount = Treatment.objects.filter(doctor=did,istreated=False).count()
    print trecount,untrecount
    return render(request,'navbar/doctordashboard.html',{"trecount":trecount,"untrecount":untrecount})

def treatedpatientsview(request):
    return render(request,'navbar/treatedpatients.html',{"treated":1})

def nontreatedpatientsview(request):
    return render(request,'navbar/nontreatedpatients.html',{"treated":0})

class getAdminListview(ListAPIView):
    lookup_field = 'id'
    serializer_class = adminserializer
    queryset = Profile.objects.filter(user_type_id=1)


class get_Branches_listview(ListAPIView):
    lookup_field = 'id'
    # serializer_class = userserializer
    serializer_class = branchserializer
    queryset = Branch.objects.all()

class get_corp_listview(ListAPIView):
    lookup_field ='id'
    serializer_class = corporate_branchserializer
    queryset = Corporate.objects.all()


class get_Physician_listview(ListAPIView):
    # permission_classes = (Isadminpage,)
    lookup_field = 'staff_id'
    # serializer_class = userserializer
    serializer_class = staffserializer
    queryset = Staff.objects.filter(pro__user_type=3)
class get_Branches_listview(ListAPIView):
    lookup_field = 'id'
    # serializer_class = userserializer
    serializer_class = branchserializer
    queryset = Branch.objects.all()

class get_Nurse_listview(ListAPIView):
    # permission_classes = (Isadminpage,)
    lookup_field = 'staff_id'
    # serializer_class = userserializer
    serializer_class = staffserializer
    queryset = Staff.objects.filter(pro__user_type=2)

class get_MedTech_listview(ListAPIView):
    # permission_classes = (Isadminpage,)
    lookup_field = 'staff_id'
    # serializer_class = userserializer
    serializer_class = staffserializer
    queryset = Staff.objects.filter(pro__user_type=5)

class Rud_admin_details_view(DestroyAPIView):
    lookup_field = 'user_id'
    serializer_class = adminserializer
    queryset = Profile.objects.all()

class Rud_doctor_details_view(RetrieveUpdateDestroyAPIView):
    lookup_field = 'staff_id'
    serializer_class = DoctoreditSerializer
    queryset = Staff.objects.all()

def staff_profile_view(request,staff_id):
    print 'doctor user id'
    u = User.objects.get(id=request.user.id)
    superuser = u.is_superuser

    # obj = permission_req(Isadminpage(), request, view=None)
    if True:
        sr = Staff.objects.get(staff_id =staff_id)
        name =sr.pro.first_name+" "+sr.pro.middle_name+' '+sr.pro.last_name
        phone = sr.pro.phone
        if sr.pro.user_type.id==2:
            user = "Nurse"
        elif sr.pro.user_type.id==3:
            user = "Doctor"
        elif sr.pro.user_type.id==5:
            user = "MedTech"
        return render(request, 'navbar/staff_profile.html',{"staff_id": staff_id,"email":sr.staff.email,"name":name,
                      "phone":phone,"qualification":sr.pro.Qualification,"speciality": sr.speciality,"gender":sr.pro.gender,
                      "experience":sr.Experience,"licencenumber":sr.Licence_number,"branchcode":sr.branch_code,"user":user,"superuser":superuser})
    else:
        return HttpResponse("not have authority")

class getstaffProfile(RetrieveAPIView):
    # permission_classes = (Isadminpage,)
    lookup_field = 'staff_id'
    # serializer_class = userserializer
    serializer_class = staffserializer
    queryset = Staff.objects.all()

class get_Patients_listview(ListAPIView):
    lookup_field = 'pat_id'
    serializer_class = patientserializer
    queryset = Patient.objects.all()

class Rud_corphr_details_view(RetrieveUpdateDestroyAPIView):
    lookup_field = 'hr_id'
    serializer_class = CorphreditSerializer
    queryset = CorporateHR.objects.all()

class Createcorporatehrid(CreateAPIView):
    serializer_class = corphrserializer

class get_corp_hr(ListAPIView):
    lookup_field = 'id'
    serializer_class = corphrserializer
    queryset = CorporateHR.objects.all()

def CorpHR_profile_view(request, hr_id):
    print 'doctor user id'
    u = User.objects.get(id=request.user.id)
    superuser = u.is_superuser

    # obj = permission_req(Isadminpage(), request, view=None)
    if True:
        sr = CorporateHR.objects.get(hr_id=hr_id)

        name = sr.pro.first_name + " " + sr.pro.middle_name + ' ' + sr.pro.last_name
        phone = sr.pro.phone
        email=sr.hr.email
        employee_code =sr.employee_code
	branch_code =sr.branch_name
        if sr.pro.user_type.id == 6:
            user = "Corporate HR"

        return render(request, 'navbar/corphr_profile.html',
                      {"hr_id": hr_id,  "name": name,
                       "phone": phone,"email":email,
                       'employee_code':employee_code,
			"Designation":sr.Designation,
                        "gender": sr.pro.gender,"branch_code":branch_code,
                       "branchcode": sr.branch_code,
                       "user": user,"superuser":superuser})
    else:
        return HttpResponse("not have authority")





class link_patient_view(RetrieveUpdateDestroyAPIView):
    lookup_field = 'patient_code'
    queryset = Patient.objects.all()
    serializer_class = Patientlinkserializer

    # def get_object(self):
    #     pk = self.request.data["patient_code"]
    #     return Patient.objects.get(patient_code=pk)  # or request.PO
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        doc = request.data["doctorid"]
        nodoc = []
        for did in doc:
            doctor = get_or_none(Staff,staff_id=did)
            print doctor
            if doctor:
                try:
                    t = Treatment.objects.get(doctor=doc[0],patient=instance.pat_id)
                except Exception:
                    t=None
                tre = Treatment()
                
                if t:
                    if t.istreated==1:
                        tre.istreated=0
                        tre.save
                if t is None:
                    tre.doctor_id = did
                    tre.patient = instance.pat_id
                    tre.save()
            else:
                nodoc.append(str(did))
        if len(nodoc)>0 :
            return Response({"message": "doctor with {} id doesnot exist ".format(','.join(nodoc)), "code": -1}, status=404)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response({"message":"success","code":1},status=200)


class get_patients_doctor(ListAPIView):
    lookup_field = 'patient_code'
    queryset = Patient.objects.all()
    serializer_class = patientserializer

    def get(self, request, *args, **kwargs):
        tred = request.GET.get("istreated",None)
        typep = request.GET.get("patient_type",None)
        queryset =self.get_queryset()
        print queryset
        if typep == "Corporate" and tred is not None:
            id=request.user.id
            hr=CorporateHR.objects.get(hr_id=id)
            br=hr.branch_code
            queryset = self.get_queryset().filter(patient_type=typep,corporate_code=br)
            print queryset
            tpatlis=Treatment.objects.filter(istreated=tred)
            # print tpatlis.queryset_set.all()

            pobjs=[]
            tobjs =[]
            for i in list(tpatlis):
                tobjs.append(i.patient)

            for i in list(queryset):
                if i.pat_id in tobjs:
                    pobjs.append(i)
            page = self.paginate_queryset(pobjs)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(pobjs, many=True)
            return Response(serializer.data)
        elif typep == "Corporate" and tred is None:
            id=request.user.id
            hr=CorporateHR.objects.get(hr_id=id)
            br=hr.branch_code
            queryset = self.get_queryset().filter(patient_type=typep,corporate_code=br)
            pobjs=[]
            tobjs =[]
            tpatlis=Treatment.objects.all()
            for i in list(tpatlis):
                tobjs.append(i.patient)

            for i in list(queryset):
                if i.pat_id not in tobjs:
                    pobjs.append(i)
            page = self.paginate_queryset(pobjs)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(pobjs, many=True)
            return Response(serializer.data)
        elif typep is None and tred is None:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        # print tred
        user = request.user.id
        lispatient =[]
        tre = Treatment.objects.filter(doctor=user, istreated=tred)
        for obj in list(tre):
            lispatient.append(obj.patient)
        doc = Staff.objects.get(staff_id=user)
        queryset = doc.patient_set.all()
        finallis =[]
        for i in list(queryset):
            if i.pat_id in lispatient:
                finallis.append(i)
        page = self.paginate_queryset(finallis)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(finallis, many=True)
        return Response(serializer.data)
        # return Response(list(finallis))


class get_doctors_patient(ListAPIView):
    lookup_field = 'patient_code'
    queryset = Patient.objects.all()
    serializer_class = getpatientserializer

    def get(self, request, *args, **kwargs):
        patient_code = self.kwargs.get(self.lookup_field)
        query = Patient.objects.get(patient_code=patient_code)
        queryset = query.doc_link.all()
        lis = []
        for i in list(queryset):
            dic = {}
            dic["doctorid"] = i.staff_id
            dic["name"] = i.pro.first_name + ' ' + i.pro.middle_name + ' ' + i.pro.last_name
            dic["speciality"] = i.speciality
            lis.append(dic)
        return Response(lis)


class get_physician_nurse(ListAPIView):
    lookup_field = 'staff_id'
    queryset = Staff.objects.all()
    serializer_class = getphysiciannurse

    def get(self, request, *args, **kwargs):
        sid = self.kwargs.get(self.lookup_field)

        obj = Staff.objects.get(staff_id=sid)
        branch = obj.branch_code
        queryset = Staff.objects.filter(branch_code__icontains=str(branch), pro__user_type_id=3)
        lis = []
        for i in list(queryset):
            dic = {}
            dic["doctorid"] = i.staff_id
            dic["name"] = i.pro.first_name + ' ' + i.pro.middle_name + ' ' + i.pro.last_name
            dic["speciality"] = i.speciality
            dic["branchcode"] = str(branch)
            lis.append(dic)
        return Response(lis)




class get_Physician_listview(ListAPIView):
    # permission_classes = (Isadminpage,)
    lookup_field = 'staff_id'
    serializer_class = staffserializer
    queryset = Staff.objects.filter(pro__user_type=3)
    def get(self,request, *args,**kwargs):
        data = request.GET
        info = model_meta.get_field_info(Staff)
        dictonary = get_querystring_params(data,info)
        queryset = self.get_queryset()
        if data.get('branch_code',None):
            print "Dssdsd"
            queryset =queryset.filter(**dictonary).annotate(
                doctor_id=(F('staff__id')),name= Concat(F('pro__first_name'),Value(' '),F('pro__middle_name'),Value(' '),F('pro__last_name'))).values('branch_code','name','speciality','doctor_id')
            return Response(queryset)
        else:
            print "eneer"
            queryset = queryset.filter(**dictonary)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


def patientsummary(request, pat_id):
    context = {}
    u = Profile.objects.get(user_id=request.user.id)
    userfor = u.user_type_id
    if userfor == 3:
        context.update({"drsummary": 1})
    if userfor == 3:
        try:
            tre = Treatment.objects.get(patient=pat_id, doctor=request.user.id)
        except Exception:
            tre = None
        if tre:    
            treated = tre.istreated
            context["treated"] = treated

    docpre = Doctorpresciption.objects.filter(patient=pat_id)
    doctherepaticpre = DoctorTherepaticpresciption.objects.filter(patient_t=pat_id)
    userinfo = Userinfosummary.objects.filter(user_id=pat_id).last()
    medicalinfoforpatient = Medicationlogs.objects.filter(user_id=pat_id, Doctor=None)
    patdosage = []
    for i in medicalinfoforpatient:
        patdosage.append(i.Dosage)
    medicalinfo = Medicationlogs.objects.filter(user_id=pat_id).exclude(Doctor=None)
    dosage = []
    for i in medicalinfo:
        dosage.append(i.Dosage)
    riskvalues = Risk_sore.objects.filter(user_id=pat_id).last()
    userperson = evaluation_form.objects.filter(user_id=pat_id).last()
    usr = pat_id
    print usr, 'dddd'
    user = Patient.objects.get(pat_id=usr)
    phid = user.PHID
    corpo_id = user.corporate_code
    emp_id = user.employee_id
    print user.patient_code, 'sss'
    if user.patient_code:
        userglucos = glucos.objects.filter(patient_code=user.patient_code).last()
        useroximeter = oximeter.objects.filter(patient_code=user.patient_code).last()
        usertemp = Temperature.objects.filter(patient_code=user.patient_code).last()
        # print usertemp.temperature,"usertemp"
        userbpm = Bpmmeter.objects.filter(patient_code=user.patient_code).last()
        userweight = Weightmeter.objects.filter(patient_code=user.patient_code).last()
        userspirometer = Spirometery.objects.filter(patient_code=user.patient_code).last()
        ldlparamenter = Ldlmeter.objects.filter(patient_code=user.patient_code).last()
        himoblogin = Himobloginmeter.objects.filter(patient_code=user.patient_code).last()
        hbac1 = Hbacmeter.objects.filter(patient_code=user.patient_code).last()
        triglecyridea = Triglecyridesmeter.objects.filter(patient_code=user.patient_code).last()
        urinedata = Urinemeter.objects.filter(patient_code=user.patient_code).last()

        ecg12data = EcgNIGmeter.objects.filter(patient_code=user.patient_code).last()
        ecgdata = Ecgmeter.objects.filter(patient_code=user.patient_code).last()
    else:
        userglucos = glucos.objects.filter(patient_code=user.patient_code).last()
        useroximeter = oximeter.objects.filter(patient_code=user.patient_code).last()
        usertemp = Temperature.objects.filter(patient_code=user.patient_code).last()
        userbpm = Bpmmeter.objects.filter(patient_code=user.patient_code).last()
        userweight = Weightmeter.objects.filter(patient_code=user.patient_code).last()
        userspirometer = Spirometery.objects.filter(patient_code=user.patient_code).last()
        ldlparamenter = Ldlmeter.objects.filter(patient_code=user.patient_code).last()
        himoblogin = Himobloginmeter.objects.filter(patient_code=user.patient_code).last()
        hbac1 = Hbacmeter.objects.filter(patient_code=user.patient_code).last()
        triglecyridea = Triglecyridesmeter.objects.filter(patient_code=user.patient_code).last()
        urinedata = Urinemeter.objects.filter(patient_code=user.patient_code).last()

        ecg12data = EcgNIGmeter.objects.filter(patient_code=user.patient_code).last()
        ecgdata = Ecgmeter.objects.filter(patient_code=user.patient_code).last()

    if riskvalues:
        urebmi = riskvalues.bmi
        if riskvalues.diabetes_score is not None:
            dialevel, dialevelmeasure = summriskpre.diabdiaplay(riskvalues.diabetes_score)
        else:
            dialevel, dialevelmeasure = 'Not Available', ''

        if riskvalues.hyper_score is not None:
            print riskvalues.hyper_score
            hyperlevel, hyperlevelmeasure = summriskpre.hyperdiaplay(riskvalues.hyper_score)
        else:
            hyperlevel, hyperlevelmeasure = 'Not Available', ''
        if riskvalues.heart_score is not None:
            heartlevel, heartlevelmeasure = summriskpre.heartdiaplay(riskvalues.heart_score, userperson.gender)
        else:
            heartlevel, heartlevelmeasure = 'Not Available', ''
            print heartlevel
        if userperson.obesity == "yes":
            obeysitylevel = 'Diagnosed'
            obeysitylevelmeasure = ' '
        else:
            obeysitylevel, obeysitylevelmeasure = summriskpre.obesitybdiaplay(riskvalues.bmi, userperson.ethnicity)
            if userperson.hypertension == "yes":
                hyperlevel = 'Diagnosed'
    else:
        riskunavailable = None
        context.update({"user": user, 'userinfo': userinfo, 'useroximeter': useroximeter, 'userglucos': userglucos,
                        'usertemp': usertemp, 'userbpm': userbpm, 'medicalinfo': medicalinfo, "docpre": docpre,"doctherepaticpre":doctherepaticpre,
                        'userperson': userperson, "riskunavailable": riskunavailable, "phid": phid,
                        "corpo_id": corpo_id, "emp_id": emp_id,
                        "ldlparamenter": ldlparamenter, "himoblogin": himoblogin, "hbac1": hbac1,
                        "userspirometer": userspirometer,
                        "triglecyridea": triglecyridea, "urinedata": urinedata, "ecgdata": ecgdata,
                        "ecg12data": ecg12data, "medidosageinpat": patdosage,
                        "medicalinfoforpatient": medicalinfoforpatient, })

        return render(request, 'navbar/patientsummaryindoctor.html', context)

    context.update({"user": user, 'userinfo': userinfo, 'useroximeter': useroximeter, 'userglucos': userglucos,
                    'usertemp': usertemp, 'userbpm': userbpm, 'medicalinfo': medicalinfo,
                    'dialevel': dialevel, 'dialevelmeasure': dialevelmeasure,
                    'hyperlevel': hyperlevel, "docpre": docpre,"doctherepaticpre":doctherepaticpre,
                    'hyperlevelmeasure': hyperlevelmeasure,
                    'heartlevel': heartlevel, "medidosageinpat": patdosage,
                    "medicalinfoforpatient": medicalinfoforpatient,
                    'heartlevelmeasure': heartlevelmeasure,
                    'obeysitylevel': obeysitylevel, "phid": phid, "corpo_id": corpo_id, "emp_id": emp_id,
                    'obeysitylevelmeasure': obeysitylevelmeasure, 'userperson': userperson,
                    "userbmi": urebmi, "ldlparamenter": ldlparamenter, "himoblogin": himoblogin, "hbac1": hbac1,
                    "userspirometer": userspirometer,
                    "triglecyridea": triglecyridea, "urinedata": urinedata, "ecgdata": ecgdata, "ecg12data": ecg12data,
                    "medidosage": dosage})

    return render(request, 'navbar/patientsummaryindoctor.html', context)

class doctorPresciption(View):
    def post(self,request,*args,**kwargs):
        docobj = Doctorpresciption()
        docobj.prescription = request.POST.get('presciption')
        docobj.patient = request.POST.get('docpatientid')
        pat_id = docobj.patient
        print 'sssssssss',docobj.patient
        pre = docobj.prescription
        a = request.user.id
        # cdate =timezone.now()
        cdate= request.POST.get('cdate')
        print 'date ',cdate
        dpro = Profile.objects.get(user_id = a)
        print "",dpro

        docobj.createdDate=cdate
        docobj.docname= dpro.first_name+" "+dpro.middle_name+" "+dpro.last_name
        name = docobj.docname
        print 'wwwwww',name
        docobj.save()
        try:
            tre = Treatment.objects.get(doctor=request.user.id, patient=pat_id)
        except Exception:
            tre=None
        if tre:
            tre.istreated = True
            tre.save()
        return redirect(reverse_lazy('usermanagement:patientsummaryindoctor', args=(int(pat_id),)))

class savethearapicrpatient(View):
    def post(self, request, *args, **kwargs):
        docobj = DoctorTherepaticpresciption()
        docobj.prescription_t = request.POST.get('presciption_t')
        docobj.patient_t = request.POST.get('docpatientid_t')
        
        pat_id = docobj.patient_t
        print 'sssssssss', docobj.patient_t
        pre = docobj.prescription_t
        a = request.user.id
        # cdate =timezone.now()
        cdate = request.POST.get('cdate_t')
        print 'date ', cdate
        dpro = Profile.objects.get(user_id=a)
        print dpro
        # docobj.doctor = request.user.id
        docobj.createdDate_t = cdate
        docobj.docname_t = dpro.first_name + " " + dpro.middle_name + " " + dpro.last_name
        name = docobj.docname_t
        print 'wwwwww', name
        docobj.save()

        try:
            tre = Treatment.objects.get(doctor=request.user.id, patient=pat_id)
        except Exception:
            tre=None
        if tre :
            tre.istreated = True
            tre.save()
        return redirect(reverse_lazy('usermanagement:patientsummaryindoctor', args=(int(pat_id),)))
class savemedication(LoginRequiredMixin,View):
    # def get(self, request):
    #     return render(request,'summary-result.html')
    def post(self, request):
        obj=Medicationlogs()
        obj.user_id=request.POST.get('patientid')
        pat_id =request.POST.get('patientid')
        obj.PrescriptionDate=request.POST.get('PrescriptionDate')
        obj.MedicationName = request.POST.get('MedicationName')
        obj.TMR_of_medicine = request.POST.get('tmr_of_medicine')
        obj.HWT_of_medicine = request.POST.get('hwt_of_medicine')
        # obj.Doctor = request.user.id
        doc = Staff.objects.get(staff_id=request.user.id)
        obj.Doctor = doc.pro.first_name+' '+doc.pro.middle_name+' '+doc.pro.last_name
        # lis_of_dos = [request.POST.get('Dosage'),request.POST.get('ExtraDosage1'),request.POST.get('ExtraDosage2'),request.POST.get('ExtraDosage3'),request.POST.get('ExtraDosage4')]
        #
        # lis_of_tim = [request.POST.get('timmings'),request.POST.get('ExtraTimmings1'),request.POST.get('ExtraTimmings2'),request.POST.get('ExtraTimmings3'),request.POST.get('ExtraTimmings4')]
        # for i,j in zip(lis_of_tim,lis_of_dos):
        #     if i == None or j == None:
        #         lis_of_tim.remove(i)
        #         lis_of_dos.remove(j)
        #     else:
        #         d = datetime.strptime(i, "%H:%M")
        #         ind = lis_of_tim.index(i)
        #         i = d.strftime("%I:%M %p")
        #         lis_of_tim[ind] = i
        obj.Dosage = request.POST.get('dosage')
        #obj.timmings =','.join(lis_of_tim)
        obj.WithFood = request.POST.get('WithFood')
        obj.Reason = request.POST.get('Reason')
        obj.Reactions = request.POST.get('reaction')
        obj.TMR_of_medicine = request.POST.get('tmr_of_medicine')
        obj.HWT_of_medicine = request.POST.get('hwt_of_medicine')

        obj.save()
        return redirect(reverse_lazy('usermanagement:patientsummaryindoctor', args=(int(pat_id),)))

def corporatehr_view(request):
    u = User.objects.get(id=request.user.id)
    user = u.is_superuser
    context={}
    if user ==1:
        context["user"]="superadmin"
    else:
        context["user"]=None
    return render(request, 'navbar/corporate_hr.html',context)

def hrdashboard_view(request):
    id = request.user.id
    hr = CorporateHR.objects.get(hr_id=id)
    br = hr.branch_code
    plist = Patient.objects.filter(corporate_code=br, patient_type="Corporate")
    untre = []
    tre = []
    tpatlis = Treatment.objects.all()
    context ={"treated": '',"untreatcount":0,"treatcount":0,"unassingcount":0}
    for i in list(tpatlis):
        if i.istreated == 0:
            untre.append(i.patient)
        elif i.istreated == 1:
            tre.append(i.patient)
    for i in plist:
        if i.pat_id in untre:
            context["untreatcount"] = context.get('untreatcount', 0)+1
        elif i.pat_id in tre:
            context["treatcount"] = context.get('treatcount', 0) + 1
        else:
            context["unassingcount"] = context.get('unassingcount', 0) + 1
    # print context
    context["tcount"]=plist.count()
    return render(request, 'navbar/hrdashboard.html',context)
    # return render(request, 'navbar/hrdashboard.html',{"treated":''})

def corporatepatientsview(request,path):
    # print path
    # id=request.user.id
    # hr=CorporateHR.objects.get(hr_id=id)
    # br=hr.branch_code
    # plist=Patients.objects.filter(corporate_code=br)
    # untre=Treatment.objects.filter(istreated=0)
    # tre=Treatment.objects.filter(istreated=1)
    # pobjs=[]
    # for i in plist:
    #     if path=='untreated':
    #         obj=untre.get(patient=i)
    #         pobjs.append(obj)
    #     else:
    #         obj=tre.get(patient=i)
    #         pobjs.append(obj)

    if path =="treated":
        treated=1
        type="Corporate"
    elif path == "unassigned":
        treated=2
        type="unassign"
    else:
        treated=0
        type="Corporate"
    return render(request, 'navbar/corporatepatients.html',{"treated":treated,"type":type})

def patientsummary_in_corporate_hr_view(request,pat_id):
    print pat_id
    docpre = Doctorpresciption.objects.filter(patient=pat_id)
    userinfo=Userinfosummary.objects.filter(user_id=request.user.id).last()
    medicalinfo=Medicationlogs.objects.filter(user_id=pat_id)
    dosage = []
    for i in medicalinfo:
        dosage.append(i.Dosage)
    riskvalues = Risk_sore.objects.filter( user_id=pat_id).last()
    userperson=evaluation_form.objects.filter(user_id=pat_id).last()
    usr = pat_id
    print usr,'dddd'
    user = Patient.objects.get(pat_id=usr)
    print user.patient_code,'sss'
    if user.patient_code:
        userglucos = glucos.objects.filter(patient_code=user.patient_code).last()
        useroximeter = oximeter.objects.filter(patient_code=user.patient_code).last()
        usertemp = Temperature.objects.filter(patient_code=user.patient_code).last()
        # print usertemp.temperature,"usertemp"
        userbpm = Bpmmeter.objects.filter(patient_code=user.patient_code).last()
        userweight = Weightmeter.objects.filter(patient_code=user.patient_code).last()
        userspirometer = Spirometery.objects.filter(patient_code=user.patient_code).last()
        ldlparamenter= Ldlmeter.objects.filter(patient_code=user.patient_code).last()
        himoblogin=Himobloginmeter.objects.filter(patient_code=user.patient_code).last()
        hbac1 =Hbacmeter.objects.filter(patient_code=user.patient_code).last()
        triglecyridea =Triglecyridesmeter.objects.filter(patient_code=user.patient_code).last()
        urinedata=Urinemeter.objects.filter(patient_code=user.patient_code).last()

        ecg12data = EcgNIGmeter.objects.filter(patient_code=user.patient_code).last()
        ecgdata=Ecgmeter.objects.filter(patient_code=user.patient_code).last()

    else:
        userglucos = glucos.objects.filter(patient_code=user.patient_code).last()
        useroximeter = oximeter.objects.filter(patient_code=user.patient_code).last()
        usertemp = Temperature.objects.filter(patient_code=user.patient_code).last()
        userbpm = Bpmmeter.objects.filter(patient_code=user.patient_code).last()
        userweight = Weightmeter.objects.filter(patient_code=user.patient_code).last()
        userspirometer = Spirometery.objects.filter(patient_code=user.patient_code).last()
        ldlparamenter = Ldlmeter.objects.filter(patient_code=user.patient_code).last()
        himoblogin = Himobloginmeter.objects.filter(patient_code=user.patient_code).last()
        hbac1 = Hbacmeter.objects.filter(patient_code=user.patient_code).last()
        triglecyridea = Triglecyridesmeter.objects.filter(patient_code=user.patient_code).last()
        urinedata = Urinemeter.objects.filter(patient_code=user.patient_code).last()
        ecg12data = EcgNIGmeter.objects.filter(patient_code=user.patient_code).last()
        ecgdata=Ecgmeter.objects.filter(patient_code=user.patient_code).last()

    if riskvalues:
        urebmi = riskvalues.bmi
        if riskvalues.diabetes_score is not None:
            dialevel, dialevelmeasure = summriskpre.diabdiaplay(riskvalues.diabetes_score)
        else:
            dialevel, dialevelmeasure =  'Not Available',''
        if riskvalues.hyper_score is not None:
            print riskvalues.hyper_score
            hyperlevel, hyperlevelmeasure = summriskpre.hyperdiaplay(riskvalues.hyper_score)
        else:
            hyperlevel, hyperlevelmeasure =  'Not Available',''
        if riskvalues.heart_score is not None:
            heartlevel, heartlevelmeasure = summriskpre.heartdiaplay(riskvalues.heart_score,userperson.gender)
        else:
            heartlevel, heartlevelmeasure =  'Not Available',''
            print heartlevel
        if userperson.obesity =="yes":
            obeysitylevel = 'Diagnosed'
        else:
            obeysitylevel, obeysitylevelmeasure = summriskpre.obesitybdiaplay(riskvalues.bmi, userperson.ethnicity)
	    if userperson.hypertension =="yes":
	        hyperlevel = 'Diagnosed'

    return render(request, 'navbar/patientsummary_in_corporate_hr.html',{"user":user,'userinfo': userinfo, 'useroximeter': useroximeter, 'userglucos': userglucos,
                    'usertemp': usertemp, 'userbpm': userbpm, 'medicalinfo': medicalinfo,
                    'dialevel': dialevel, 'dialevelmeasure': dialevelmeasure,
                    'hyperlevel': hyperlevel,"docpre":docpre,
                    'hyperlevelmeasure': hyperlevelmeasure,
                    'heartlevel': heartlevel,
                    'heartlevelmeasure': heartlevelmeasure,
                    'obeysitylevel': obeysitylevel,
                    'obeysitylevelmeasure': obeysitylevelmeasure, 'userperson': userperson,
                    "userbmi": urebmi,"ldlparamenter":ldlparamenter,"himoblogin":himoblogin,"hbac1":hbac1,"userspirometer":userspirometer,
                    "triglecyridea":triglecyridea,"urinedata":urinedata,"ecgdata":ecgdata,"ecg12data":ecg12data,"medidosage":dosage})

def patienthealthanalysisinHR(request,analysis):
    user = request.user.id
    hr = CorporateHR.objects.get(hr_id=user)
    # patients = Patient.objects.filter(corporate_code=hr.branch_code).latest("updated_0n")
    #
    # sds = Patient.objects.filter(corporate_code="FRE").values('pat_id')
    # print sds
    query = Risk_sore.objects.filter(user__in=Subquery(
        Patient.objects.filter(corporate_code=hr.branch_code).values('pat_id'),
    )).values().annotate(Max("updated_0n")).order_by(F("updated_0n").desc())
    # # print query.query
    #
    # query.group_by=['user_id']
    # results = QuerySet(query=query, model=Risk_sore)
    # print query
    # query.group_by = ['user_id',]
    # print query
    # print type(query)

    # query ="SELECT `healthandrecords_risk_sore`.`score_id`, `healthandrecords_risk_sore`.`user_id`, `healthandrecords_risk_sore`.`diabetes_score`, `healthandrecords_risk_sore`.`heart_score`, `healthandrecords_risk_sore`.`hyper_score`, `healthandrecords_risk_sore`.`h_per`, `healthandrecords_risk_sore`.`bmi`, MAX(`healthandrecords_risk_sore`.`updated_0n`) FROM `healthandrecords_risk_sore` WHERE`healthandrecords_risk_sore`.`user_id` IN (SELECT U0.`pat_id` FROM `usermanagement_patient` U0 WHERE U0.`corporate_code` = 'FRE') GROUP BY `healthandrecords_risk_sore`.`user_id` ORDER BY `healthandrecords_risk_sore`.`updated_0n` DESC;"
    # results = QuerySet(query=query, model=Risk_sore)
    #
    # sasa = results.values()


    # print results
    #.values('user_id','updated_0n').annotate(date = Max("updated_0n"))
    #.order_by(F("updated_0n").desc()).distinct("user_id")
    # risk_pat = Risk_sore.objects.filter(updated_0n_in=Subquery(
    #     query.values('updated_0n')
    # ))
    lis=[]
    seen = set()
    risk_id =[]
    for i in query:
        if i["user_id"] not in seen:
            risk_id.append(i["score_id"])
            lis.append(i)
            seen.add(i["user_id"])
    riskpats = Risk_sore.objects.filter(score_id__in=risk_id).annotate(
        PHID=Subquery(Patient.objects.filter(pat_id=OuterRef('user_id')).values("PHID")),
        patientname=Subquery(
            Patient.objects.filter(pat_id=OuterRef('user_id')).annotate(
                patientname=Concat(F("pro__first_name"), Value(" "), F("pro__middle_name"), Value(" "), F("pro__last_name"))
                                                                                         ).values("patientname")),
        employeeId=Subquery(Patient.objects.filter(pat_id=OuterRef('user_id')).values("employee_id")),
        gender=Subquery(Patient.objects.filter(pat_id=OuterRef('user_id')).values("pro__gender")),
        patientId=Subquery(Patient.objects.filter(pat_id=OuterRef('user_id')).values("pat_id")),
        ethincity=Subquery(evaluation_form.objects.filter(user_id=OuterRef('user_id')).values("ethnicity")[:1]),
    ).values()
    context = {}
    # print riskpats
    dic={"hyper":[],"heart":[],"diabetes":[],"obesity":[]}
    context["details"]=[]
    for object in riskpats:
        dic["hyper"].append(hyperdiaplay(object.get("hyper_score",None))[0])
        dic["heart"].append(heartdiaplay(object.get("heart_score",None),object.get("gender"))[0])
        dic["diabetes"].append(diabdiaplay(object.get("diabetes_score",None))[0])
        dic["obesity"].append(obesitybdiaplay(object.get("bmi",None),object.get("ethincity",None))[0])
        context["details"].append({
            "patientname": object["patientname"],
            "update": object["updated_0n"],
            "patientId":object["patientId"],
            "PHID":object["PHID"],
            "gender":object["gender"],
            "ethincity":object["ethincity"],
            "employeeId":object["employeeId"],
            "hyper":str(hyperdiaplay(object.get("hyper_score",None))[0]),
            "heart":str(heartdiaplay(object.get("heart_score",None),object.get("gender"))[0]),
            "diabetes":str(diabdiaplay(object.get("diabetes_score",None))[0]),
            "obesity":str(obesitybdiaplay(object.get("bmi",None),object.get("ethincity",None))[0])
        })


    context["heart_score"]={
            str("Low"):dic["heart"].count("Low"),
            str("Moderate"):dic["heart"].count("Moderate"),
            str("High"):dic["heart"].count("High"),
            str("Diagnosed"):dic["heart"].count("Diagnosed")
        }
    context["diabetes_score"]={
            "Low":dic["diabetes"].count("Low"),
            "Moderate":dic["diabetes"].count("Moderate"),
            "High":dic["diabetes"].count("High"),
            "Diagnosed":dic["diabetes"].count("Diagnosed")
        }
    context["hyper_score"]={
            "Low":dic["hyper"].count("Low"),
            "Moderate":dic["hyper"].count("Moderate"),
            "High":dic["hyper"].count("High"),
            "Diagnosed":dic["hyper"].count("Diagnosed")
        }
    context["obesity_score"]= {
            "Underweight": dic["obesity"].count("Underweight"),
            "Normal": dic["obesity"].count("Normal"),
            "Overweight": dic["obesity"].count("Overweight"),
            "Pre_Obese": dic.get("obesity",[]).count("Pre-Obese"),
            "Obese": dic["obesity"].count("Obese")
        }
    # print  context["details"]
    print context["heart_score"]
    # context["treated"]=2
    # context["type"]='unassign'
    return render(request,"navbar/healthanalysis{0}.html".format(analysis),context)
