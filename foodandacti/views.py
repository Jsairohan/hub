# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views import View
from .models import Medicationlogs,Userinfosummary,activitysecduled,Food_details,usersfoodsdairy,recipefoods,setgoalsd,fit_ex
from apiforapp.models import *
from healthandrecords.models import evaluation_form,Risk_sore
from foodandacti.models import setgoalsd
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.db.models import Sum
from django.utils.decorators import method_decorator
from beforelogin.models import User
from .calculators import Claries
from datetime import date#datetime.date.today
import datetime
from insuranceandcygen.decko import dash_compleletd
from django.contrib.auth.decorators import login_required
from foodandacti import summriskpre
from django.http import JsonResponse
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import DeleteView,UpdateView
from django.views.generic.detail import SingleObjectMixin
from django import template
from collections import OrderedDict
from foodandacti.models import *
# Create your views here.
def foodupdateview(request,pk):
    obj = usersfoodsdairy.objects.filter(user_id=request.user.id)
    obj=obj.filter(id=pk).last()

    if obj.isconsumed:
        obj.isconsumed=None
    else:
        obj.isconsumed = "checked"
    obj.save()
    print  pk,"objid", obj.isconsumed
    return redirect(reverse_lazy("foodandacti:personal_info_update"))

def fooddeleteview(request,pk):

    obj = usersfoodsdairy.objects.filter(user_id=request.user.id).filter(id=pk)
    obj.delete()

    return redirect(reverse_lazy("foodandacti:personal_info_update"))

def activiesupdateview(request,pk):
    obj = activitysecduled.objects.filter(user_id=request.user.id)
    obj = obj.filter(id=pk).last()

    if obj.isperformed:
        obj.isperformed = ""
    obj.isperformed = "checked"
    obj.save()
    return redirect(reverse_lazy("foodandacti:activityredirct"))


# class FoodDeleteview(DeleteView):
#     model = usersfoodsdairy
#     success_url = reverse_lazy("foodandacti:fooddelete")
#
#
#
# class ActiviesDeleteview(DeleteView):
#     model = activitysecduled
#     success_url = reverse_lazy("foodandacti:activitydelete")



def Activityredirct(request):
    return redirect(reverse('foodandacti:createactivity', kwargs={'slug':'Monday'}))

class completesummaryview(LoginRequiredMixin,View):
    @method_decorator(dash_compleletd)
    def get(self, request):
        # print request.user.id,'user_id'

        # print request.user.id,'user_id'
        docpre = Doctorpresciption.objects.filter(patient=request.user.id)
        doctherepaticpre = DoctorTherepaticpresciption.objects.filter(patient_t=request.user.id)
        userinfo = Userinfosummary.objects.filter(user_id=request.user.id).last()
        medicalinfoforpatient = Medicationlogs.objects.filter(user_id=request.user.id,Doctor=None)
        patdosage = []
        for i in medicalinfoforpatient:
            patdosage.append(i.Dosage)
        medicalinfo = Medicationlogs.objects.filter(user_id=request.user.id).exclude(Doctor=None)
        dosage = []
        for i in medicalinfo:
            dosage.append(i.Dosage)
        riskvalues = Risk_sore.objects.filter(user_id=request.user.id).last()
        userperson = evaluation_form.objects.filter(user_id=request.user.id).last()
        usr = request.user.id
        print usr, 'dddd'
        user = Patient.objects.get(pat_id=usr)
        print user.patient_code, 'sss'
        name = user.pro.first_name + ' ' + user.pro.middle_name + ' ' + user.pro.last_name
        phid=user.PHID
	corpo_id = user.corporate_code
        emp_id =user.employee_id
        
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
            obeysitylevel,obeysitylevelmeasure = 'Diagnosed',''
	else:
            obeysitylevel, obeysitylevelmeasure = summriskpre.obesitybdiaplay(riskvalues.bmi, userperson.ethnicity)
	if userperson.hypertension =="yes":
	    hyperlevel,hyperlevelmeasure  = 'Diagnosed',''
        

        # return render(request, 'navbar/summarykc.html',
        #               {'userinfo': userinfo, 'useroximeter': useroximeter, 'userglucos': userglucos,
        #                'usertemp': usertemp, 'userbpm': userbpm, 'medicalinfo': medicalinfo,
        #                'dialevel': dialevel, 'dialevelmeasure': dialevelmeasure,
        #                'hyperlevel': hyperlevel,
        #                'hyperlevelmeasure': hyperlevelmeasure,
        #                'heartlevel': heartlevel,
        #                'heartlevelmeasure': heartlevelmeasure,
        #                'obeysitylevel': obeysitylevel,
        #                'obeysitylevelmeasure': obeysitylevelmeasure, 'userperson': userperson,
        #                "userbmi": riskvalues.bmi,"ldlparamenter":ldlparamenter,"himoblogin":himoblogin,"hbac1":hbac1,"userspirometer":userspirometer,
		# 	"triglecyridea":triglecyridea,"urinedata":urinedata,"ecgdata":ecgdata,"ecg12data":ecg12data,"medidosage":dosage})
        return render(request, 'navbar/summarykc.html',
                      {'userinfo': userinfo, 'useroximeter': useroximeter, 'userglucos': userglucos,
                       'usertemp': usertemp, 'userbpm': userbpm, 'medicalinfo': medicalinfo,
                       'dialevel': dialevel, 'dialevelmeasure': dialevelmeasure,
                       'hyperlevel': hyperlevel, "docpre": docpre,"doctherepaticpre":doctherepaticpre,
                       'hyperlevelmeasure': hyperlevelmeasure,
                       'heartlevel': heartlevel,"phid":phid,"corpo_id":corpo_id , "emp_id":emp_id,
                       'heartlevelmeasure': heartlevelmeasure,
                       'obeysitylevel': obeysitylevel,"medidosageinpat":patdosage,"medicalinfoforpatient":medicalinfoforpatient,
                       'obeysitylevelmeasure': obeysitylevelmeasure, 'userperson': userperson,
                       "userbmi": riskvalues.bmi, "ldlparamenter": ldlparamenter, "himoblogin": himoblogin,
                       "hbac1": hbac1, "userspirometer": userspirometer,
                       "triglecyridea": triglecyridea, "urinedata": urinedata, "ecgdata": ecgdata,
                       "ecg12data": ecg12data, "medidosage": dosage, "patientName": name})


class usersummarypostview(LoginRequiredMixin,View):

    # def get(self, request):
    #     return render(request,'summary-result.html')

    def post(self, request):
        obj=Userinfosummary()
        userdetails=Profile.objects.get(user_id=request.user.id)
        user = User.objects.get(id=request.user.id)
        userperson=evaluation_form.objects.filter(user_id=request.user.id).last()
        obj.user=user
        obj.name=userdetails.first_name
        obj.email = user.email
        obj.PhoneNo = userdetails.phone
        obj.age = userperson.age
        obj.Gender = userperson.gender
        obj.Address = request.POST.get('Address')
        obj.hospitalAddress = request.POST.get('hospitalAddress')
        obj.guardianname = request.POST.get('guardianname')
        obj.ContactNo = request.POST.get('ContactNo')
        obj.gAddress = request.POST.get('gAddress')
        obj.Doctorname = request.POST.get('Doctorname')
        obj.Doctornumb = request.POST.get('Doctornumb')
        obj.MaritalStatus = userperson.maritial_status
        obj.EmployedStatus = userperson.employment
        obj.HousingStatus = userperson.housing_status

        obj.allergy = request.POST.get('allergy')
        obj.save()
        return redirect(reverse_lazy('foodandacti:summary'))


class mediclummarypostview(LoginRequiredMixin,View):

    # def get(self, request):
    #     return render(request,'summary-result.html')

    def post(self, request):
        obj=Medicationlogs()
        obj.user=User.objects.get(id=request.user.id)
        obj.PrescriptionDate=request.POST.get('PrescriptionDate')
        obj.MedicationName = request.POST.get('MedicationName')
        obj.Doctor = request.POST.get('Doctor')
        # lis_of_dos = [request.POST.get('Dosage'),request.POST.get('ExtraDosage1'),request.POST.get('ExtraDosage2'),request.POST.get('ExtraDosage3'),request.POST.get('ExtraDosage4')]
        #
        # print lis_of_dos,"dosage"
        #
        obj.TimesPerDay = request.POST.get('TimesPerDay')
        # lis_of_tim = [request.POST.get('timmings'),request.POST.get('ExtraTimmings1'),request.POST.get('ExtraTimmings2'),request.POST.get('ExtraTimmings3'),request.POST.get('ExtraTimmings4')]
        # print'timings',lis_of_tim
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
        # obj.timmings =','.join(lis_of_tim)
        obj.WithFood = request.POST.get('WithFood')
        obj.Reason = request.POST.get('Reason')
        obj.Reactions = request.POST.get('reaction')
        obj.TMR_of_medicine = request.POST.get('tmr_of_medicine')
        obj.HWT_of_medicine = request.POST.get('hwt_of_medicine')
        obj.save()
        return redirect(reverse_lazy('foodandacti:summary'))




@login_required(login_url="/login/")
def foodform1(request):
    print request.build_absolute_uri(),'build_absolute_uri'
    id = request.user.id
    method_dict = request.GET.get('date', None)
    print method_dict

    if request.method=='POST':
        obj = usersfoodsdairy()
        obj.user = User.objects.get(id=id)

        obj.fodd_name = request.POST.get("foodnames")
        obj.wheninday = request.POST.get("sectionmel")
        obj.Calories = request.POST.get("Calories")
        obj.Carbs = request.POST.get("Carbs")
        obj.Protein = request.POST.get("Protiens")
        obj.Fat = request.POST.get("Fat")
        print obj.fodd_name,obj.Calories,obj.Carbs,obj.Protein,obj.Fat

        if method_dict:
            print method_dict, 'hhhhhhhhhhhhhhh'
            obj.fooddate = method_dict
            obj.save()
            return redirect(reverse('foodandacti:personal_info_update')+'?date={}'.format(method_dict))#
        else:
            print method_dict, 'hhhhhhhhhhhhhhh'
            obj.fooddate = date.today()
            obj.save()
            # print 'i amam gere'

            return redirect(reverse('foodandacti:personal_info_update'))


def foodform(request,pk):
    id = request.GET.get('pk', None)
    result=Food_details.objects.get(pk=pk)
    data = {
        'size':result.Calories,
        'foodname':result.fodd_name,
        'fat':result.Fat,
    'carbs':result.Carbs,
    'protein':result.Protein
    }
    data = data
    return JsonResponse(data)

# def get_bruntcal():
class UserActivityscheduleCreate(LoginRequiredMixin,View):
    slug_url_kwarg='slug'

    @method_decorator(dash_compleletd)
    def get(self, request, *args, **kwargs):
        slug = kwargs.get(self.slug_url_kwarg)
        asecdule=activitysecduled.objects.filter(dayofweek=slug).filter(user_id=request.user.id)
        daylist=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

        return render(request,'navbar/activitiessingle.html',{'daylist':daylist,'asecdule':asecdule,'slug':slug})

    def post(self, request, *args, **kwargs):
        myist= [41, 45, 50, 54, 59, 64, 68, 73, 77, 82, 86, 91, 100, 109, 118, 127, 136]

        slug = kwargs.get(self.slug_url_kwarg)
        obj = activitysecduled()
        slug = kwargs.get(self.slug_url_kwarg)
        obj.user = User.objects.get(id=request.user.id)
        obj.dayofweek=slug
        obj.exercise = request.POST.get('Activity')
        obj.howtime = request.POST.get('Duration')
        userweight = evaluation_form.objects.filter(user_id=request.user.id).last()
        xweight=min(myist, key=lambda x: abs(x - int(userweight.weight) ))

        activity = float(fit_ex.objects.get(activity__iexact=str(obj.exercise)).kg_50)*(int(userweight.weight)  / 50.0)*(int(obj.howtime)/30.0)
        obj.calburnt = activity

        obj.save()
        return redirect(reverse('foodandacti:createactivity', kwargs={'slug':slug}))

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

def getcalneeded(curweight,expentwieght,gender,time,userid,person_details):
    calobj = Claries()

    calobj.gender = person_details.gender
    calobj.height = int(((int(person_details.h_feet)*(12)+int(person_details.h_inches)) * (2.54)))
    calobj.weight = int(person_details.weight)
    calobj.age = int(person_details.age)
    calobj.activity = 0
    calobj.time = 1

    calobj.target_time=time
    # print curweight , expentwieght
    if int(curweight) < int(expentwieght):
        calobj.target = int(expentwieght) - int(curweight) 
        if person_details.gender == 'Male':
            b = calobj.cal_men_gian()
        else:
            b = calobj.cal_women()
        change_type = 'gain'
        return [change_type, b]
    elif int(curweight) >= int(expentwieght):
        calobj.target = int(expentwieght) - int(curweight)
        if person_details.gender == 'Male':
            b = calobj.cal_men_loss()
        else:
            b = calobj.cal_women_loss()
        change_type = 'lose'
        return [change_type, b]

# print 90.0>95

class SetgoalCreate(LoginRequiredMixin,CreateView):
    @method_decorator(dash_compleletd)
    def get(self, request, *args, **kwargs):
        slug = kwargs.get(self.slug_url_kwarg)
        # print slug
        asecdule=setgoalsd.objects.filter(user_id=request.user.id).last()
        userweight = evaluation_form.objects.filter(user_id=request.user.id).last()
        daylist=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

        return render(request,'navbar/extendgoalset.html',{'weight':userweight.weight,'asecdule':asecdule})

    def post(self, request, *args, **kwargs):

        obj=setgoalsd.objects.filter(user_id=request.user.id).last()
        if obj:
            obj=obj
        else:
            obj = setgoalsd()
        food_dex = fit_ex.objects.all()
        userweight= evaluation_form.objects.filter(user_id=request.user.id).last()
        # print request.user.id,'user id'
        obj.user = User.objects.get(id=request.user.id)
        obj.targetnumberkg = request.POST.get('weight')
        obj.targetdays = request.POST.get('time')
        a,b=getcalneeded(userweight.weight,obj.targetnumberkg,userweight.gender,obj.targetdays,request.user.id,userweight)
        # print a,b,'change','cla need',obj.targetnumberkg,userweight.gender
        obj.change_type = a

        obj.calneeded = b

        # obj.targetdays = request.POST.get('time')


        obj.save()
        print obj.targetnumberkg,obj.targetdays,obj.change_type
        return redirect(reverse_lazy("healthandrecords:health_ana"))



def updateviews(request,slug):
    date = request.session["date"]
    usersfoodsdairy.objects.filter(sluged=slug).delete()
    return redirect('profile/update/?date={}'.format(date))


@csrf_exempt
def fooddetails_search(request):
    if request.method=='POST':

        searchtext=request.POST['search_text']
    else:
        searchtext=''
    print searchtext
    # a='indian'
    # b='sounth indian'
    # recipe = fs.foods_search('puri')

    lis=[]
    food_dex = Food_details.objects.order_by('fodd_name')

    food_de11=food_dex.filter(fodd_name__istartswith=searchtext)
    food_del2 = food_dex.filter(fodd_name__icontains=searchtext)
    lis.extend(list(food_de11))
    lis.extend(list(food_del2))


    res = list(OrderedDict.fromkeys(lis))


    #food_de1=food_dex.filter(fodd_name__icontains=searchtext).distinct()

    return render(request, 'navbar/auto_search.html', {'object_list': res})

def isfood_goal_acti_good(dayofweek,id):
    print dayofweek
    dailtgoal = setgoalsd.objects.filter(user_id=id).last()
    if dailtgoal:
        goaltype = dailtgoal.change_type
        daylist = [['Sunday', 6], ['Monday', 0], ['Tuesday', 1], ['Wednesday', 2], ['Thursday', 3], ['Friday', 4],
                   ['Saturday', 5]]
        for i in daylist:
            if dayofweek == i[1]:
                newweekday = i[0]
        cultburt = activitysecduled.objects.filter(user_id=id).filter(dayofweek=newweekday).aggregate(
            Sum('calburnt')).get(
            'calburnt__sum')
        if cultburt:
            cultburt = cultburt
        else:
            cultburt = 0
        if dailtgoal.change_type=='gain':
            # dayofweek
            # print activitysecduled.objects.filter(user_id=id).filter(dayofweek=newweekday).aggregate(Sum('calburnt')),'goaldddddddaaaaaaaaaay'
            dailtcal = dailtgoal.calneeded + cultburt
        else:
            dailtcal = dailtgoal.calneeded - cultburt
    else:
        bmr=evaluation_form.objects.filter(user_id=id).last().bmr

        daylist = [['Sunday', 6], ['Monday', 0], ['Tuesday', 1], ['Wednesday', 2], ['Thursday', 3], ['Friday', 4],
                   ['Saturday', 5]]
        for i in daylist:
            if dayofweek == i[1]:
                newweekday = i[0]
        cultburt = activitysecduled.objects.filter(user_id=id).filter(dayofweek=newweekday).aggregate(
            Sum('calburnt')).get(
            'calburnt__sum')
        if cultburt:
            cultburt = cultburt
        else:
            cultburt = 0

            # dayofweek
            # print activitysecduled.objects.filter(user_id=id).filter(dayofweek=newweekday).aggregate(Sum('calburnt')),'goaldddddddaaaaaaaaaay'
        dailtcal = bmr + cultburt
    return dailtcal

class personal_info_update(LoginRequiredMixin,ListView):
    model = usersfoodsdairy
    context_object_name = 'notifications'
    template_name = 'navbar/dietsingle.html'

    @method_decorator(dash_compleletd)
    def get(self, request, *args, **kwargs):
        # method_dict = request.GET.get('date', None)
        # print method_dict,'hhhhhhhhhhhhhhh'
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        # for i in context:
        #     print i
        if context:
            #print 'i amm hereeeeeeee'
            return self.render_to_response(context)
        else:
            return render(request, self.template_name)


    def get_context_data(self, **kwargs):
        id = self.request.user.id
        lidaylist=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

        method_dict = self.request.GET.get('date', None)
        if method_dict:
            method_dict=method_dict
            a = method_dict.split('-')
            a = datetime.datetime(int(a[0]), int(a[1]), int(a[2]))
            dayofweek=a.weekday()
        else:
            method_dict = date.today()
            dayofweek =date.today().weekday()

        context = super(personal_info_update,self).get_context_data(**kwargs)#super(ArticleListView, self).get_context_data(**kwargs)
        indayof=self.model.objects.filter(user_id=id).filter(fooddate=method_dict)
        context['Breakfast'] = indayof.filter(wheninday="Breakfast")
        context['Lunch'] = indayof.filter(wheninday="Lunch")
        context['Dinner'] = indayof.filter(wheninday="Dinner")
        context['Snacks'] = indayof.filter(wheninday="Snacks")
	context['exercise']=evaluation_form.objects.filter(user_id=id).last().exercise
	context['gender'] = evaluation_form.objects.filter(user_id=id).last().gender
        context['h_feet'] = evaluation_form.objects.filter(user_id=id).last().h_feet
        context['h_inches'] = evaluation_form.objects.filter(user_id=id).last().h_inches
        context['weight'] = evaluation_form.objects.filter(user_id=id).last().weight
        context['age'] =  evaluation_form.objects.filter(user_id=id).last().age


	target = setgoalsd.objects.filter(user_id=id).last()
        if target is not None:
            context['targetnumberkg'] = setgoalsd.objects.filter(user_id=id).last().targetnumberkg
        else:
            context['targetnumberkg'] = evaluation_form.objects.filter(user_id=id).last().weight

        	

        context['newdaily']=abs(isfood_goal_acti_good(dayofweek,id))

        return context


@login_required(login_url="/login/")
@dash_compleletd
def personal_info(request):
    userinfo = Userinfosummary.objects.filter(user_id=request.user.id).last()
    medicalinfo = Medicationlogs.objects.filter(user_id=request.user.id)
    riskvalues = Risk_sore.objects.filter(user_id=request.user.id).last()
    userperson = evaluation_form.objects.filter(user_id=request.user.id).last()

    if request.user.patient_code:
        userglucos = glucos.objects.filter(patient_code=request.user.patient_code).last()
        useroximeter = oximeter.objects.filter(patient_code=request.user.patient_code).last()
        usertemp = Temperature.objects.filter(patient_code=request.user.patient_code).last()
        userbpm = Bpmmeter.objects.filter(patient_code=request.user.patient_code).last()
        userweight = Weightmeter.objects.filter(patient_code=request.user.patient_code).last()
        userspirometer = Spirometery.objects.filter(patient_code=request.user.patient_code).last()
    else:
        userglucos = glucos.objects.filter(patient_code=request.user.patient_code).last()
        useroximeter = oximeter.objects.filter(patient_code=request.user.patient_code).last()
        usertemp = Temperature.objects.filter(patient_code=request.user.patient_code).last()
        userbpm = Bpmmeter.objects.filter(patient_code=request.user.patient_code).last()
        userweight = Weightmeter.objects.filter(patient_code=request.user.patient_code).last()
        userspirometer = Spirometery.objects.filter(patient_code=request.user.patient_code).last()

    if riskvalues.diabetes_score is not None:
        dialevel, dialevelmeasure = summriskpre.diabdiaplay(riskvalues.diabetes_score)
    else:
        dialevel, dialevelmeasure =  'Not Available',''
    if riskvalues.hyper_score is not None:
        hyperlevel, hyperlevelmeasure = summriskpre.hyperdiaplay(riskvalues.hyper_score)
    else:
        hyperlevel, hyperlevelmeasure = 'Not Available',''

    if riskvalues.heart_score is not None:
        heartlevel, heartlevelmeasure = summriskpre.heartdiaplay(riskvalues.heart_score, userperson.gender)
    else:
        heartlevel, heartlevelmeasure = 'Not Available', ''
    
    if userperson.obesity =="Yes":
        obeysitylevel = 'Diagnosed'
    else:
        obeysitylevel, obeysitylevelmeasure = summriskpre.obesitybdiaplay(riskvalues.bmi, userperson.ethnicity)
    return render(request, 'navbar/summarykc.html',
                  {'userinfo': userinfo, 'useroximeter': useroximeter, 'userglucos': userglucos,
                   'usertemp': 'usertemp', 'userbpm': 'userbpm', 'medicalinfo': medicalinfo,
                   'dialevel': dialevel, 'dialevelmeasure': dialevelmeasure,
                   'hyperlevel': hyperlevel,
                   'hyperlevelmeasure': hyperlevelmeasure,
                   'heartlevel': heartlevel,
                   'heartlevelmeasure': heartlevelmeasure,
                   'obeysitylevel': obeysitylevel,
                   'obeysitylevelmeasure': obeysitylevelmeasure, 'userperson': userperson, "userbmi": riskvalues.bmi})



# def foodactivityview(request):
#     method_dict = request.GET.get('date', None)
#     if method_dict:
#         method_dict = method_dict
#         a = method_dict.split('-')
#         a = datetime.datetime(int(a[0]), int(a[1]), int(a[2]))
#         dayofweek = a.weekday()
#     else:
#         method_dict = date.today()
#         dayofweek = date.today().weekday()
#     todays = date.today()
#     daylist = [['Sunday', 6], ['Monday', 0], ['Tuesday', 1], ['Wednesday', 2], ['Thursday', 3], ['Friday', 4],
#                ['Saturday', 5]]
#
#     weekdaytoday = date.today().weekday()
#     for i in daylist:
#         if weekdaytoday == i[1]:
#             newweekday = i[0]
#     indayof = usersfoodsdairy.objects.filter(user_id=id).filter(fooddate=todays)
#     newdaily = isfood_goal_acti_good(weekdaytoday, id)
#     eval_data = evaluation_form.objects.filter(user_id=id).last()
#     Breakfast = indayof.filter(wheninday="Breakfast")
#     Lunch = indayof.filter(wheninday="Lunch")
#
#     Dinner = indayof.filter(wheninday="Dinner")
#     Snacks = indayof.filter(wheninday="Snacks")
#     asecdule = activitysecduled.objects.filter(dayofweek=newweekday).filter(user_id=request.user.id)
#     return render(request, 'navbar/activities_new.html',
#                   {
#                    'asecdule': asecdule,
#                    'Breakfast': Breakfast, 'Lunch': Lunch, 'Dinner': Dinner, 'Snacks': Snacks, "newdaily": newdaily,
#                    "eval_data": eval_data, "newweekday": newweekday})
