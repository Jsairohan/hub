# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from insuranceandcygen.decko import dash_compleletd
from .models import *
from django.core.cache import cache
from .diabetes_risk_score import *
from django.forms.models import model_to_dict
from beforelogin.views import Geter_cache
from .cardiac_risk_scores import *
from beforelogin.models import User
from insuranceandcygen.decko import dash_compleletd
from calculators import Claries, Bmr, Bfp
from django.urls import reverse_lazy
from datetime import date
from foodandacti.models import activitysecduled, usersfoodsdairy, setgoalsd
from foodandacti.views import isfood_goal_acti_good
from foodandacti import summriskpre
from datetime import date, timedelta
from django.utils import timezone


# Create your views here
#
# .

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


@login_required(login_url="/login/")
@dash_compleletd
def pre_meas(request):
    return render(request, 'navbar/fullpreventive.html')


@login_required(login_url="/login/")
@dash_compleletd
def pre_meas(request):
    return render(request, 'navbar/fullpreventive.html')


@login_required(login_url="/login/")
@dash_compleletd
def health_ana(request):
    # person_details = get_or_none(Profileinfo, uid=id)

    id = request.user.id
    a = Risk_sore.objects.filter(user_id=id).last()

    # profile = Geter_cache(id=id, tables=evaluation_form, user_speci="profile_details",
    #                     user_dic=cache.get(id)).users_cache_speci()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    dia_score = a.diabetes_score
    h_score, h_per = a.heart_score, a.h_per
    print h_score
    bp_score = a.hyper_score
    daily_input = Today_hel.objects.filter(user_id=id)
    # print daily_input
    if daily_input:
        print daily_input
        context = daily_input
        daily_input = Today_hel.objects.filter(user_id=id)[:7]
        if daily_input:
            b = daily_input
        else:
            b = Today_hel.objects.filter(uid=id)
        c = [[], [], [], [], [], []]
        for i in b:
            try:
                c[0].append(i.updated_0n.strftime("%Y-%m-%d"))
                c[1].append(int(i.systo))
                c[2].append(int(i.diasto))
                c[3].append(int(i.gluc))
                c[4].append(int(i.helath_hdl))
                c[5].append(int(i.health_tc))
            except:
                pass

    else:
        c = [[], [], [], [], [], []]

    # print c dashboardkc  navbar1
    todays = date.today()
    daylist = [['Sunday', 6], ['Monday', 0], ['Tuesday', 1], ['Wednesday', 2], ['Thursday', 3], ['Friday', 4],
               ['Saturday', 5]]

    weekdaytoday = date.today().weekday()
    for i in daylist:
        if weekdaytoday == i[1]:
            newweekday = i[0]
    indayof = usersfoodsdairy.objects.filter(user_id=id).filter(fooddate=todays)
    eval_data = evaluation_form.objects.filter(user_id=id).last()
    newdaily = abs(isfood_goal_acti_good(weekdaytoday, id))

    Breakfast = indayof.filter(wheninday="Breakfast")
    Lunch = indayof.filter(wheninday="Lunch")

    Dinner = indayof.filter(wheninday="Dinner")
    Snacks = indayof.filter(wheninday="Snacks")
    asecdule = activitysecduled.objects.filter(dayofweek=newweekday).filter(user_id=request.user.id)

    date_time = todays - timezone.timedelta(days=7)
    asecdule1 = activitysecduled.objects.filter(user_id=request.user.id, createdDate__gte=date_time)
    print asecdule1
    days_clak = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [],
                 "Sunday": []}
    lis_cal = []
    for i in asecdule1:
        days_clak[str(i.dayofweek)].append(i.calburnt)

    for h in days_clak:
        days_clak[h] = sum(days_clak[h])

    lis = [days_clak["Monday"], days_clak["Tuesday"], days_clak["Wednesday"], days_clak["Thursday"],
           days_clak["Friday"], days_clak["Saturday"], days_clak["Sunday"]]

    goaltarget = setgoalsd.objects.filter(user_id=request.user.id).last()
    if goaltarget:
        if goaltarget.editeedon:
            dayspasses = date.today() - goaltarget.editeedon
            dayspasses = dayspasses.days
    else:
        dayspasses = 0

    date_time = date.today() - timezone.timedelta(days=7)
    dailcalgoal = usersfoodsdairy.objects.filter(user_id=request.user.id, fooddate__gte=date_time)
    days_clak = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [],
                 "Sunday": []}
    target = setgoalsd.objects.filter(user_id=request.user.id).last()
    for i in dailcalgoal:
        we = (i.fooddate).strftime('%A')
        days_clak[we].append(float(i.Calories))
    calneed = []
    # f = float(target.calneeded)
    f = 899
    for su in days_clak:
        days_clak[su] = round(sum(days_clak[su]), 3)
        calneed.append(round(f, 3))
    calburnt = [days_clak["Monday"], days_clak["Tuesday"], days_clak["Wednesday"], days_clak["Thursday"],
                days_clak["Friday"], days_clak["Saturday"], days_clak["Sunday"]]

    calntbunt = ((calneed[0] * 35) / 100)
    l = []
    for i in calburnt:
        if i < calntbunt:
            l.append(1)
        elif i > f:
            l.append(2)
        else:
            l.append(3)

    t = (calburnt, calneed, l)
    print t

    return render(request, 'navbar/dashboardkc.html',
                  {'bp_score': bp_score, 'h_score': h_score,
                   'dia_score': dia_score, 'bmi': a.bmi, 'todayhel': c, 'asecdule': asecdule, "goaltarget": goaltarget,
                   'Breakfast': Breakfast, 'Lunch': Lunch, 'Dinner': Dinner, 'Snacks': Snacks, "newdaily": newdaily,
                   "eval_data": eval_data, "newweekday": newweekday,
                   "dayspasses": dayspasses, "listcalburnt": lis, "list_for_calburnt": calburnt,
                   "list_for_calneedtobe": calneed, "list_for_colors": l})


# if bp_score is not None else ''


@login_required(login_url="/login/")
def Cyegn_packs(request):
    user = request.user
    id = user.id
    context = ''
    return render(request, 'navbar/hospital_packages_simple.html')


@login_required(login_url="/login/")
def Hosptila_packs(request):
    hospitals1 = []
    hospitals2 = []
    hospitals = cache.get('hospitals')
    if not hospitals:
        Hospitals = Hospital.objects.all()
        cache.set('hospitals', Hospitals, 120)
        hospitals = cache.get('hospitals')
    for i in range(len(hospitals)):
        if i % 2 != 0:
            hospitals1.append(hospitals[i])
        else:
            hospitals2.append(hospitals[i])

    return render(request, 'navbar/extend_hospitalpacks.html', {'hospitals1': hospitals1, 'hospitals2': hospitals2})


@login_required(login_url="/login/")
def evaluation_form_view_details_editer(request):
    return render(request, 'navbar/evaluation_formkc.html')


@login_required(login_url="/login/")
def evaluation_form_view_details(request):
    id = request.user.id
    obj = evaluation_form.objects.filter(user_id=id).last()
    # print obj,'evaluation_form_model'
    if request.method == "POST":
        obj = evaluation_form()
        risk_obj = Risk_sore()

        obj.user = User.objects.get(id=id)
        # print request.POST.get('age')
        obj.age = int(request.POST.get('age'))
        obj.weight = float(request.POST.get('weight'))
        obj.h_feet = request.POST.get('h_feet')
        obj.h_inches = request.POST.get('h_inch')
        obj.gender = request.POST.get('gender')
        obj.smoker = request.POST.get('smoker')
        obj.bp_systolic = request.POST.get('systolic')
        obj.bp_diastolic = request.POST.get('diastolic')
        obj.anualincome = request.POST.get('annualincome')
        obj.employment = request.POST.get('employment')
        obj.maritial_status = request.POST.get('maritialstatus')
        obj.housing_status = request.POST.get('housingstatus')
        obj.ethnicity = request.POST.get('Ethnicity')
        obj.family_diabetes = request.POST.get('familydiabetes')
        obj.hypertension = request.POST.get('hypertension')
        # print request.POST.get('waistcircumference')
        obj.waist_circumference = (request.POST.get('waistcircumference'))
        obj.exercise = request.POST.get('exercise')
        obj.geostational_diabetes = request.POST.get('geostationaldia')
        obj.treated_for_systolic_bp = request.POST.get('treatedforsystolicbp')
        obj.hdl_level = request.POST.get('hdllevel')
        obj.total_cholestoral = request.POST.get('totalcholestoral')
        final_hdl_level = int(18 * (int(obj.hdl_level)))

        final_totalcholestoral = int(18 * (int(obj.total_cholestoral)))

        obj.save()
        exercise1 = obj.exercise
        if exercise1 == 'little_exercise':
            exer = 1.200
        elif exercise1 == 'Light_exercise':
            exer = 1.375
        elif exercise1 == 'Moderate_exercise':
            exer = 1.550
        elif exercise1 == 'Heavy_exercise':
            exer = 1.775
        else:
            exer = 1.900

        h1 = int(obj.h_feet)
        h2 = int(obj.h_inches)
        height_in_inches = (((h1 * 12) + (h2)))
        height_in_cm = (height_in_inches) * (2.54)
        print('height_in_centimeters', height_in_cm)
        height_in_meters = ((height_in_inches) * (0.0254)) ** 2
        # print height_in_meters
        bmi = float(float(obj.weight) / (height_in_meters))
        # print bmi
        bmrmy = Bmr()
        bmrmy.age = int(obj.age)
        bmrmy.weight = int(obj.weight)
        bmrmy.height = float(height_in_cm)
        bmrmy.exercise = exer
        bmrmy.gender = obj.gender
        if obj.gender == 'Male':
            b = bmrmy.men_bmr()
        else:
            b = bmrmy.women_bmr()
        obj.bmr = b

        obj.save()

        risk_obj.bmi = bmi
        for i in [obj.gender, obj.age, obj.smoker, obj.hdl_level, obj.bp_systolic,
                  obj.total_cholestoral, obj.treated_for_systolic_bp]:
            print i, "caricac test"

        if all([obj.gender, obj.age, obj.smoker, obj.hdl_level, obj.bp_systolic,
                obj.total_cholestoral, obj.treated_for_systolic_bp]):
            h_score, h_per = gender_1(gender=obj.gender.title(), age=obj.age, smoker=obj.smoker.title(),
                                      hdl_level=final_hdl_level,
                                      systolic=int(obj.bp_systolic),
                                      totalcholestoral=final_totalcholestoral,
                                      treated_for_systolic_bp=obj.treated_for_systolic_bp)
            risk_obj.heart_score = h_score
            risk_obj.h_per = h_per
            print h_score, h_per
        else:
            pass

        if all([obj.age, obj.smoker, obj.bp_systolic,
                obj.waist_circumference,
                obj.gender]):
            def is_hyper(age=obj.age, smoker=obj.smoker, systolic=int(obj.bp_systolic),
                         waist_circumference=int(obj.waist_circumference), gender=obj.gender,
                         ):
                if obj.hypertension == 'Yes':
                    bp_score = -1
                else:
                    bp_score = hyper(age=obj.age, smoker=obj.smoker.title(), systolic=int(obj.bp_systolic),
                                     waist_circumference=int(obj.waist_circumference),
                                     gender=obj.gender.title())

                return bp_score

            bp_score = is_hyper(age=obj.age, smoker=obj.smoker.title(), systolic=int(obj.bp_systolic),
                                waist_circumference=int(obj.waist_circumference),
                                gender=obj.gender.title(),
                                )
            risk_obj.hyper_score = bp_score
        else:
            pass
        a = [obj.age, obj.gender, obj.weight, height_in_inches, obj.exercise, obj.family_diabetes,
             obj.hypertension]
        for i in a:
            print i, "dia betes test", str(i)
        if all([obj.age, obj.gender, obj.weight, height_in_inches, obj.exercise, obj.family_diabetes,
                obj.hypertension]):
            def dia_gender(age=obj.age, weight=obj.weight, height=height_in_inches,
                           exercise=obj.exercise.title(),
                           diabetes=obj.family_diabetes.title(),
                           gender=obj.gender.title(), hypertension=obj.hypertension,
                           f_diabetes=obj.geostational_diabetes):
                if gender == 'Male':
                    dia_score = men_dia(age=obj.age, weight=obj.weight, height=height_in_inches,
                                        exercise=obj.exercise.title() if obj.exercise else None,
                                        diabetes=obj.family_diabetes.title(),
                                        hypertension=obj.hypertension)
                else:
                    dia_score = women_dia(age=obj.age, weight=obj.weight, height=height_in_inches,
                                          exercise=obj.exercise.title() if obj.exercise else None,
                                          diabetes=obj.family_diabetes.title(),
                                          hypertension=obj.hypertension,
                                          f_diabetes=obj.geostational_diabetes)
                return dia_score

            dia_score = dia_gender(age=obj.age, weight=obj.weight, height=height_in_inches,
                                   exercise=obj.exercise.title() if obj.exercise else None,
                                   diabetes=obj.family_diabetes.title() if obj.diabetes else None,
                                   hypertension=obj.hypertension,
                                   gender=obj.gender.title(),
                                   f_diabetes=obj.geostational_diabetes)
            risk_obj.diabetes_score = dia_score
        else:
            pass
        risk_obj.user = obj.user
        risk_obj.save()
        dict_obj = model_to_dict(obj)
        return redirect(reverse_lazy('foodandacti:summary'))

    elif request.method == 'GET':
        profile_details = obj

        if profile_details:

            return render(request, 'navbar/evaluation_result.html', {"eval_data": profile_details})
            # elif not profile_details.patient_code and profile_details:


        else:
            return render(request, 'navbar/evaluation_formkc.html')


# @login_required(login_url="/login/")
# def first_form(request):
#     id = request.user.id
#     print id,'userid'
#     # uid=user.id
#     # form = FirstForm()
#     # for i in form:
#     #     print i.field
#     # form.Height1
#     obj = get_or_none(person_form, user_id=id)
#     # risk = Risk_sore.objects.get(user_id=request.user.id)
#     if request.method == "POST":
#
#         # obj.uid=1
#         if obj:
#             obj = obj
#             risk_oj = get_or_none(Risk_sore, user_id=id)
#             obj.user = User.objects.get(id=id)
#             obj.age = int(request.POST.get('age'))
#             obj.gender = request.POST.get('Gender')
#             obj.i_feet = request.POST.get('heights')
#             obj.i_inches = request.POST.get('heights1')
#             obj.weight = float(request.POST.get('weight'))
#             obj.drinker = request.POST.get('Drinker')
#             obj.smoker = request.POST.get('smoker')
#             obj.diastolic = int(request.POST.get('Diastolic'))
#             obj.hdl = int(request.POST.get('hdl'))
#             obj.bp = int(request.POST.get('Systolic'))
#             obj.employe = request.POST.get('Employment')
#             obj.hypertension = request.POST.get('hypertension')
#             obj.m_status = request.POST.get('MaritalStatus')
#             obj.a_income = request.POST.get('AnnualIncome')
#             obj.h_status = request.POST.get('HousingStatus')
#             obj.tc = int(request.POST.get('tc'))
#             obj.exercise = request.POST.get('Exercise')
#             obj.h_cond = request.POST.get('healthc')
#             obj.treated = request.POST.get('treat')
#             obj.eat = request.POST.get('eat')
#             obj.wasit = int(request.POST.get('wasit'))
#             obj.bg = request.POST.get('bg')
#             obj.Heal_screen = request.POST.get('screening')
#             obj.diabetes = request.POST.get('Diabetes')
#             obj.f_diabetes = request.POST.get('gestational')
#             heights1, height1 = int(obj.i_feet), int(obj.i_inches)
#             height = (heights1) * 12 + height1
#             obj.hieght = height
#             bmi = float(obj.weight) / ((((height) * (0.025)) ** 2))
#             obj.bmi = bmi
#             bmrmy = Bmr()
#             bmrmy.age = int(obj.age)
#             bmrmy.weight = int(obj.weight)
#             bmrmy.height = int(height)
#             bmrmy.gender = obj.gender
#             if obj.gender == 'Male':
#                 b = bmrmy.men_bmr()
#             else:
#                 b = bmrmy.women_bmr()
#                 print b, 'tis is my bmr'
#             obj.bmr = b
#
#             obj.save()
#
#             risk_oj.bmi = bmi
#             # print height,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'
#             # print obj.i_feet,obj.i_inches,obj.drinker
#             months = ["January", "February", "March", "April", "May", "June", "July", "August", "Septembe", "October",
#                       "November", "December"]
#             # if month in months:
#             # req=User.objects.values('dom','doa','doy','gender').get(id=request.user.id)
#             # #print req
#             # g_date=req['doa']
#             # month=req['dom']
#             # year=req['doy']
#             # t_month = months.index(month)
#             # today = date.today()
#             # print today.year,year,today.month,today.day,t_month,g_date
#             # age = today.year - year - ((today.month, today.day) < (t_month, g_date))
#
#             h_score, h_per = gender_1(gender=obj.gender.title(), age=obj.age, smoker=obj.smoker.title(), hdl=obj.hdl,
#                                       bp=obj.bp, tc=obj.tc,
#                                       treat=obj.treated.title())
#             risk_oj.heart_score = h_score
#             risk_oj.h_per = h_per
#             print h_score, h_per
#
#             def is_hyper(age=obj.age, smoker=obj.smoker, bp=obj.bp, waist=obj.wasit, gender=obj.gender,
#                          hypertension=obj.hypertension):
#                 if obj.hypertension == 'Yes':
#                     bp_score = -1
#                 else:
#                     bp_score = hyper(age=obj.age, smoker=obj.smoker.title(), bp=obj.bp, waist=obj.wasit,
#                                      gender=obj.gender.title())
#
#                 return bp_score
#                 # drinker,diabetes,hypertension,exercise,bp,diastolic,
#                 # income,m_status,employment,h_status,tc,treat,hdl,h_cond,hosp_screen
#
#             bp_score = is_hyper(age=obj.age, smoker=obj.smoker.title(), bp=obj.bp, waist=obj.wasit,
#                                 gender=obj.gender.title(),
#                                 hypertension=obj.hypertension)
#
#             risk_oj.hyper_score = bp_score
#
#             def dia_gender(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                            diabetes=obj.diabetes.title(), bp=obj.bp,
#                            bg=obj.bg.title(), gender=obj.gender.title(), f_diabetes=obj.f_diabetes):
#                 if gender == 'Male':
#                     dia_score = men_dia(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                                         diabetes=obj.diabetes.title(), bp=obj.bp, bg=obj.bg.title())
#                 else:
#                     dia_score = women_dia(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                                           diabetes=obj.diabetes.title(), bp=obj.bp, bg=obj.bg.title(),
#                                           f_diabetes=obj.f_diabetes)
#
#                 return dia_score
#
#             dia_score = dia_gender(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                                    diabetes=obj.diabetes.title(),
#                                    bp=obj.bp, bg=obj.bg.title(), gender=obj.gender.title(),
#                                    f_diabetes=obj.f_diabetes)
#             # print dia_score,'dddddddddddd'
#             risk_oj.diabetes_score = dia_score
#             risk_oj.user = obj.user
#             risk_oj.save()
#             # print dia_score
#
#             obj1 = Geter_cache(id=id, updater_value=obj, user_speci='profile_details').users_cache_updater()
#             obj2 = Geter_cache(id=id, updater_value=risk_oj, user_speci='risk_score').users_cache_updater()
#             # obj={'age':age,'gender':gender,'i_feet':obj.i_feet,'i_inches':obj.i_inches,'weight':obj.weight,'drinker':obj.drinker,'smoker':obj.smoker,'diastolic':obj.diastolic,'hdl':obj.hdl}
#             dict_obj = model_to_dict(obj)
#             return redirect(reverse_lazy('foodandacti:profile'))
#
#         else:
#             obj = person_form()
#             risk_oj = Risk_sore()
#             obj.user = User.objects.get(id=request.user.id)
#             obj.age = int(request.POST.get('age'))
#             obj.gender = request.POST.get('Gender')
#             obj.i_feet = request.POST.get('heights')
#             obj.i_inches = request.POST.get('heights1')
#             obj.weight = float(request.POST.get('weight'))
#             obj.drinker = request.POST.get('Drinker')
#             obj.smoker = request.POST.get('smoker')
#             obj.diastolic = int(request.POST.get('Diastolic'))
#             obj.hdl = int(request.POST.get('hdl'))
#             obj.bp = int(request.POST.get('Systolic'))
#             obj.employe = request.POST.get('Employment')
#             obj.hypertension = request.POST.get('hypertension')
#             obj.m_status = request.POST.get('MaritalStatus')
#             obj.a_income = request.POST.get('AnnualIncome')
#             obj.h_status = request.POST.get('HousingStatus')
#             obj.tc = int(request.POST.get('tc'))
#             obj.exercise = request.POST.get('Exercise')
#             obj.h_cond = request.POST.get('healthc')
#             obj.treated = request.POST.get('treat')
#             obj.eat = request.POST.get('eat')
#             obj.wasit = int(request.POST.get('wasit'))
#             obj.bg = request.POST.get('bg')
#             obj.Heal_screen = request.POST.get('screening')
#             obj.diabetes = request.POST.get('Diabetes')
#             obj.f_diabetes = request.POST.get('gestational')
#             heights1, height1 = int(obj.i_feet), int(obj.i_inches)
#             height = (heights1) * 12 + height1
#             obj.hieght = height
#             bmi = float(obj.weight) / ((((height) * (0.025)) ** 2))
#             obj.bmi = bmi
#             bmrmy = Bmr()
#             bmrmy.age = int(obj.age)
#             bmrmy.weight = int(obj.weight)
#             bmrmy.height = int(height)
#             bmrmy.gender = obj.gender
#             if obj.gender == 'Male':
#                 b = bmrmy.men_bmr()
#             else:
#                 b = bmrmy.women_bmr()
#                 print b, 'tis is my bmr'
#             obj.bmr = b
#
#             obj.save()
#
#             risk_oj.bmi = bmi
#             # print height,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'
#             # print obj.i_feet,obj.i_inches,obj.drinker
#             months = ["January", "February", "March", "April", "May", "June", "July", "August", "Septembe", "October",
#                       "November", "December"]
#
#             h_score, h_per = gender_1(gender=obj.gender.title(), age=obj.age, smoker=obj.smoker.title(), hdl=obj.hdl,
#                                       bp=obj.bp, tc=obj.tc,
#                                       treat=obj.treated.title())
#             risk_oj.heart_score = h_score
#             risk_oj.h_per = h_per
#
#             def is_hyper(age=obj.age, smoker=obj.smoker, bp=obj.bp, waist=obj.wasit, gender=obj.gender,
#                          hypertension=obj.hypertension):
#                 if obj.hypertension == 'Yes':
#                     bp_score = -1
#                 else:
#                     bp_score = hyper(age=obj.age, smoker=obj.smoker.title(), bp=obj.bp, waist=obj.wasit,
#                                      gender=obj.gender.title())
#
#                 return bp_score
#                 # drinker,diabetes,hypertension,exercise,bp,diastolic,
#                 # income,m_status,employment,h_status,tc,treat,hdl,h_cond,hosp_screen
#
#             bp_score = is_hyper(age=obj.age, smoker=obj.smoker.title(), bp=obj.bp, waist=obj.wasit,
#                                 gender=obj.gender.title(),
#                                 hypertension=obj.hypertension)
#
#             risk_oj.hyper_score = bp_score
#
#             def dia_gender(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                            diabetes=obj.diabetes.title(), bp=obj.bp,
#                            bg=obj.bg.title(), gender=obj.gender.title(), f_diabetes=obj.f_diabetes):
#                 if gender == 'Male':
#                     dia_score = men_dia(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                                         diabetes=obj.diabetes.title(), bp=obj.bp, bg=obj.bg.title())
#                 else:
#                     dia_score = women_dia(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                                           diabetes=obj.diabetes.title(), bp=obj.bp, bg=obj.bg.title(),
#                                           f_diabetes=obj.f_diabetes.title())
#
#                 return dia_score
#
#             dia_score = dia_gender(age=obj.age, weight=obj.weight, height=height, exercise=obj.exercise.title(),
#                                    diabetes=obj.diabetes.title(),
#                                    bp=obj.bp, bg=obj.bg.title(), gender=obj.gender.title(),
#                                    f_diabetes=obj.f_diabetes)
#             # print dia_score,'dddddddddddd'
#             risk_oj.diabetes_score = dia_score
#             risk_oj.user = obj.user
#             risk_oj.save()
#             # print dia_score
#
#             obj1 = Geter_cache(id=id, updater_value=obj, user_speci='profile_details').users_cache_updater()
#             obj2 = Geter_cache(id=id, updater_value=risk_oj, user_speci='risk_score').users_cache_updater()
#             # obj={'age':age,'gender':gender,'i_feet':obj.i_feet,'i_inches':obj.i_inches,'weight':obj.weight,'drinker':obj.drinker,'smoker':obj.smoker,'diastolic':obj.diastolic,'hdl':obj.hdl}
#             dict_obj = model_to_dict(obj)
#             return redirect(reverse_lazy('foodandacti:profile'))
#
#     elif request.method == 'GET':
#         profile_details = obj
#
#         if profile_details:
#             if profile_details.patient_code:
#                 dict_obj = model_to_dict(obj)
#
#
#                 bpm = Bpmmeter.objects.filter(patient_code=profile_details.patient_code)
#                 if bpm:
#                     bpm = bpm.last()
#                 else:
#                     bpm = get_or_none(Bpmmeter, patient_code=profile_details.patient_code)
#
#                 dict_obj["bp"] = bpm.systolic
#                 dict_obj["diastolic"] = bpm.diastolic
#                 return render(request, 'navbar/newpro_result.html', {"obj": profile_details})
#             # elif not profile_details.patient_code and profile_details:
#             else:
#
#                 return render(request, 'navbar/newpro_result.html', {"obj": profile_details})
#
#         else:
#             return render(request, 'navbar/newpro.html')


@login_required(login_url="/login/")
def today_hel(request):
    if request.method == "POST":
        obj = Today_hel()
        obj.user = User.objects.get(id=request.user.id)
        obj.updated_0n = request.POST.get("date")
        obj.systo = request.POST.get("systolic")
        obj.diasto = request.POST.get("diastolic")
        obj.gluc = request.POST.get("glucose")
        obj.helath_hdl = request.POST.get("HDL")
        obj.health_tc = request.POST.get("tc")
        obj.save()
        return redirect('/healthassement/')

    return render(request, 'navbar/history_recorder.html')