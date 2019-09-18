
from healthandrecords.models import evaluation_form,Risk_sore,CheckParams
from healthandrecords.cardiac_risk_scores import *
from healthandrecords.diabetes_risk_score import *
from healthandrecords.calculators import Claries, Bmr, Bfp
from beforelogin.models import User
from django.forms.models import model_to_dict
from .models import *
from foodandacti.summriskpre import obesitybdiaplay
# from .models import CheckParams


def checknone(bpparam):
    list = []
    for i in bpparam:
        if bpparam[i]==None or bpparam[i]==0 or bpparam[i]=='' or bpparam == "0" or bpparam =='0.0':
            list.append(i)
    if list ==[]:
        return True,""
    dic = ','.join(list)
    return False,dic



def updaterisk(newrequest):
    if newrequest["exercise"]=="Little_exercise":
        newrequest["exercise"]="no"
    elif  newrequest["exercise"]=="Light_exercise":
        newrequest["exercise"] = "yes"
    elif newrequest["exercise"] == "Moderate_exercise":
        newrequest["exercise"] = "yes"
    elif newrequest["exercise"] == "Heavy_exercise":
        newrequest["exercise"] = "yes"
    elif newrequest["exercise"] == "Very_Heavy_exercise":
        newrequest["exercise"] = "yes"
    else:
        newrequest["exercise"]="yes"
    chec_obj = CheckParams()


    risk_obj = Risk_sore()
    user = User.objects.filter( id=newrequest.get("user")).last()
    h1 = int(newrequest.get("h_feet"))
    h2 = int(newrequest.get("h_inches"))
    height_in_inches = (((h1 * 12) + (h2)))
    height_in_cm = (height_in_inches) * (2.54)
    height_in_meters = ((height_in_inches) * (0.0254)) ** 2

    height_in_meters = ((float((height_in_inches) * (0.0254))) ** 2)
    bmi = float(float(newrequest.get("weight")) / (height_in_meters))
    bmrmy = Bmr()
    bmrmy.age = int(newrequest.get("age"))
    bmrmy.weight = float(newrequest.get("weight"))
    bmrmy.height = int(height_in_cm)
    bmrmy.gender = newrequest.get("gender")

    if newrequest.get("gender") == 'Male':
        b = bmrmy.men_bmr()
    else:
        b = bmrmy.women_bmr()
    newrequest["bmr"] = b



    risk_obj.bmi = bmi
    if newrequest["obesity"] == "yes" or newrequest["obesity"] == "Yes":
        chec_obj.obesity = "yes"
    else:
        d = obesitybdiaplay(bmi,newrequest["ethnicity"])
        chec_obj.obesity =d[0]
    heartparam = {
        "Gender": newrequest.get("gender"),
        "age": int(newrequest.get("age")),
        "smoker": newrequest.get("smoker"),
        "HDL": newrequest.get("hdl_level"),
        "Blood pressure": int(float(newrequest.get("bp_systolic"))),
        "Total cholestoral": newrequest.get("total_cholestoral"),
        "Treated for bp systolic ": newrequest.get("treated_for_systolic_bp"),
    }
    heartparam= checknone(heartparam)

    bpparam = {
        "age": int(newrequest.get("age")),
        "smoker": newrequest.get("smoker"),
        "Blood pressure": int(float(newrequest.get("bp_systolic"))),
        "Waist circumference": int(float(newrequest.get("waist_circumference"))),
        "Gender": newrequest.get("gender"),
    }
    bpparam= checknone(bpparam)

    diabetespara = {
        "age": int(newrequest.get("age")),
        "gender": newrequest.get("gender"),
        "weight": int(float(newrequest.get("weight"))),
        "Exercise": newrequest.get("exercise"),
        "Family diabetes": newrequest.get("family_diabetes"),
        "Hypertension": newrequest.get("hypertension"),
    }
    diabetespara= checknone(diabetespara)

    if newrequest["cardiac"] == "yes" or newrequest["cardiac"] == "Yes":
        gen = newrequest.get("gender").title()
        if gen == "Male":
            risk_obj.heart_score = 21
            risk_obj.h_per = 21
        else:
            risk_obj.heart_score = 28
            risk_obj.h_per = 28        
    else:
        if heartparam[0]:
            h_score, h_per = gender_1(gender=newrequest.get("gender").title(), age=int(newrequest.get("age")), smoker= newrequest.get("smoker").title(),
                                      hdl_level=int((float(newrequest.get("hdl_level")))),
                                      systolic=int(float(newrequest.get("bp_systolic"))),
                                      totalcholestoral=int((float(newrequest.get("total_cholestoral")))),
                                      treated_for_systolic_bp=newrequest.get("treated_for_systolic_bp").title())
            risk_obj.heart_score = h_score
            risk_obj.h_per = h_per
        else:


            chec_obj.heart_score_param = heartparam[1]



    if newrequest["hypertension"] == "yes" or newrequest["hypertension"] == "Yes":
        risk_obj.hyper_score = 6

    else:
        if bpparam[0]:
                def is_hyper(age=newrequest.get("age"), smoker=newrequest.get("smoker").title(), systolic=int(float(newrequest.get("bp_systolic"))),
                             waist_circumference=int(newrequest.get("waist_circumference")),
                             gender=newrequest.get("gender").title()
                             ):

                        bp_score = hyper(age=int(newrequest.get("age")), smoker=newrequest.get("smoker").title(), systolic=int(float(newrequest.get("bp_systolic"))),
                                         waist_circumference=int(newrequest.get("waist_circumference")),
                                         gender=newrequest.get("gender").title())

                        return bp_score

                bp_score = is_hyper(age=newrequest.get("age"), smoker=newrequest.get("smoker").title(), systolic=int(float(newrequest.get("bp_systolic"))),
                                         waist_circumference=int(newrequest.get("waist_circumference")),
                                         gender=newrequest.get("gender").title())
                risk_obj.hyper_score = bp_score
        else:

                chec_obj.hyper_score_param = bpparam[1]


    if newrequest["diabetes"] == "yes" or newrequest["diabetes"] == "Yes":
         risk_obj.diabetes_score = 11
    else:

                if diabetespara[0]:
                    def dia_gender(age=newrequest.get("age"), weight=float(newrequest.get("weight")), height=float(height_in_inches),
                                   exercise=newrequest.get("exercise").title(),
                                   diabetes=newrequest.get("family_diabetes").title(),
                                   gender=newrequest.get("gender").title(), hypertension=newrequest.get("hypertension"),
                                   f_diabetes=newrequest.get("geostational_diabetes")):
                        if gender == 'Male':
                            dia_score = men_dia(age=int(newrequest.get("age")),weight=float(newrequest.get("weight")), height=float(height_in_inches),
                                   exercise=newrequest.get("exercise").title(),
                                   diabetes=newrequest.get("family_diabetes").title(),
                                   hypertension=newrequest.get("hypertension"))
                        else:
                            dia_score = women_dia(age=int(newrequest.get("age")), weight=float(newrequest.get("weight")), height=float(height_in_inches),
                                   exercise=newrequest.get("exercise").title(),
                                   diabetes=newrequest.get("family_diabetes").title(),
                                   hypertension=newrequest.get("hypertension"),
                                   f_diabetes=newrequest.get("geostational_diabetes"))
                        return dia_score

                    dia_score = dia_gender(age=newrequest.get("age"), weight=float(newrequest.get("weight")), height=float(height_in_inches),
                                   exercise=newrequest.get("exercise").title(),
                                   diabetes=newrequest.get("family_diabetes").title(),
                                   gender=newrequest.get("gender").title(), hypertension=newrequest.get("hypertension"),
                                   f_diabetes=newrequest.get("geostational_diabetes"))
                    risk_obj.diabetes_score = dia_score
                else:

                    chec_obj.diabetes_param = diabetespara[1]

    risk_obj.user = user
    risk_obj.save()
    check = model_to_dict(risk_obj)

    chec_obj.user = user
    chec_obj.save()
    newdat=model_to_dict(chec_obj)

    return newrequest