# suhasreddy, 16:01
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from fatsecret1 import Fatsecret
from phase_1.health_form.models import
from django.contrib.auth.decorators import login_required
from .models import Foodsecd,transfor,fit_ex,Food_details,Food_details
from django.http import JsonResponse
from phase_1.curr.decko import com_compleletd,basic_compleletd,prev_compleletd,dash_compleletd

import os # import python module
from django.core.cache import cache
from .calculators import Claries,Bmr,Bfp
from phase_1.customer_health.models import Profileinfo
from django.template import RequestContext
#from django_xhtml2pdf.utils import generate_pdf
from phase_1.curr.decko import com_compleletd
from phase_1.curr.decko import com_compleletd,basic_compleletd,prev_compleletd
consumer_key='14e9c83fd3ab48c0b6406af6ba3a7d91'
consumer_secret='cfcde83284174797a311ba5e649cd972'




fs = Fatsecret(consumer_key, consumer_secret)







def get_or_none(classmodel, *kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def foodform1(request):
    method_dict = request.GET.get('date', None)

    if request.method=='POST':
        print 'ggggggggggggggggggggggggggg'
        Gender = request.POST.get("fname")
        foodnames = request.POST.get("foodnames")
        sectional = request.POST.get("sectionmel")
        sectio = request.POST.get("selfood")

        print Gender,'1',foodnames,'2',sectional,'3',sectio
        if method_dict:
            print method_dict
        else:
            print date.today()
        return render(request,'intest.html')

    return render(request,'intest.html')

def foodform(request,pk):
    id = request.GET.get('pk', None)
    print id
    result=Food_details.objects.get(pk=pk)
    data = {
        'size':result.Calories,
        'foodname':result.fodd_name
    }
    return JsonResponse(data)

@login_required(login_url="/loggin/")
@dash_compleletd
def weight(request):
    id = request.session["userid"]
    food_de = cache.get('fit_ex')
    if not food_de:
        food_dex = fit_ex.objects.all()
        cache.set('fit_ex', food_dex, 180*60)
        food_de = cache.get('fit_ex')

    # user = request.user
    # id = user.id
    if request.method == "POST":
        tra=transfor()
        obj=Claries()
        person_details=get_or_none(Profileinfo, user_id=id)
        obj.gender=person_details.Gender
        obj.height=int(person_details.rhight)*(2.54)
        obj.weight=int(person_details.Weight)
        obj.age=int(person_details.Dob)

        reqire = request.POST.get("colorRadio")
        if reqire=='gain':
            obj.target = int(request.POST.get("weight"))
            tra.weight_gain=obj.target
            obj.target_time =int( request.POST.get("time"))
            tra.gain_time=obj.target_time

            acti = request.POST.get("Activity")
            print acti
            tra.activityname=acti
            obj.activity =(float(food_de.get(activity__iexact=str(acti)).kg_50))*((obj.weight*1.0)/50)
            print obj.activity,'acacacacacacaacacac'
            tra.activity=obj.activity
            obj.time =int( request.POST.get("Duration"))
            tra.act_time=obj.time
            tra.typer='gain'
            if obj.gender=='male':
                b = obj.cal_men_gian()

            else:
                b = obj.cal_women()
            tra.calneeded=b
        elif reqire == 'lose':
            obj.target = int(request.POST.get("weightrange"))
            tra.weight_loss = obj.target
            obj.target_time = int(request.POST.get("Time"))

            tra.loss_time = obj.target_time
            acti= request.POST.get("Activity1")

            tra.activityname=acti
            obj.activity=(float(food_de.get(activity__iexact=str(acti)).kg_50))*((obj.weight*1.0)/50)

            tra.activity = obj.activity
            obj.time = int(request.POST.get("Duration1"))

            tra.act_time = obj.time

            tra.typer = 'lose'
            if obj.gender == 'male':
                b = obj.cal_men_loss()
            else:
                b = obj.cal_women_loss()
            tra.calneeded = b
        elif reqire == 'main':

            acti =request.POST.get("Activity2")
            tra.activityname=acti
            obj.activity = (float(food_de.get(activity__iexact=str(acti)).kg_50))*((obj.weight*1.0)/50)
            tra.activity = obj.activity
            obj.time = int(request.POST.get("Duration2"))
            tra.act_time = obj.time

            if obj.gender == 'male':
                b = obj.cal_men_main()
            else:
                b = obj.cal_women_main()
            tra.calneeded = b

        request.session['calneededactivity'] = tra.calneeded
        request.session['activity']=tra.activityname
        request.session['actitime']=tra.act_time

        request.session.modified = True
        tra.save()
        return render(request, 'navbar/extend_myactivity.html')
        #return redirect('/mytransform/', { 'calneeded':request.session['calneeded']})
    return render(request, 'navbar/extend_lossorgain.html')


@login_required(login_url="/loggin/")
@dash_compleletd
def food_scedule(request):
    id = request.session["userid"]
    if request.method == "POST":
        # foodsecd=Foodsecd()
        tot=request.POST.get("varity")
        breakf = request.POST.getlist("breakf")
        lunch = request.POST.getlist("lunch")
        dinner = request.POST.getlist("dinner")
        secuded=request.POST.getlist("PrescriptionDate[]")
        inthecall = request.POST.getlist("WithFood")
        #cal_food=request.POST.getlist("WithFood[]")
        #print breakf,lunch,dinner,secuded
        for i in range(0,len(breakf)):
            Foodsecd.objects.create(uid=id, breakf=breakf[i], lunch=lunch[i], dinner=dinner[i],
                                        secuded=secuded[i],ver_son=tot,cal_food=inthecall[i])

        return redirect('/food-scedule/')
    elif request.method == 'GET':
        myfood = Foodsecd.objects.filter(ver_son="meal")
        myfood = myfood.filter(uid=id)

        if myfood:
            return render(request, 'navbar/extend_mysecdule.html', {'myfood': myfood})
            #print breakf[i], lunch[i],dinner[i]
        return render(request, 'navbar/extend_foodsearch.html')