def men_dia(age, weight, height, exercise, diabetes, hypertension):
    age_p = 0
    gen_p = 1
    dia_p = 0
    bp_p = 0
    ex_p = 0
    bmi_p = 0
    # print 'diaaaaaaaaaaaaaa', type(weight), type(height)
    bmi = weight / ((((height) * (0.025)) ** 2))
    # print bmi
    m_age = {0: range(0, 40), 1: range(40, 50), 2: range(50, 60)}
    # m_bmi={0: (range(0,24 )), 1: (range(24,29 )), 2: range((29, 39))}
    for age_points, age_range in m_age.iteritems():
        if age in age_range:
            age_p = age_points
        else:
            if age > 60:
                age_p = 3
    # print age_p, "age"
    if bmi < 24:
        bmi_p = 0
    elif bmi >= 24 and bmi < 29:
        bmi_p = 1
    elif bmi >= 29 and bmi < 39:
        bmi_p = 2
    else:
        bmi_p = 3
    print bmi_p, "bmi"

    if diabetes == 'Yes':
        dia_p = 1
    else:
        dia_p = 0
    # print dia_p, "dia"
    if hypertension == 'Yes':
        bp_p = 1
    else:
        bp_p = 0
    # print bp_p, "bp"
    if exercise == 'Yes':
        ex_p = 0
    else:
        ex_p = 1
    # print ex_p, "exer"
    print age_p ,'age', bmi_p,'bmi', dia_p ,'dia', bp_p ,'hyper', ex_p ,'exer', gen_p,'gen'
    return age_p + bmi_p + dia_p + bp_p + ex_p + gen_p


def women_dia(age, weight, height, exercise, diabetes, hypertension, f_diabetes):
    # (age, weight, height, exercise, diabetes, hypertension, bg,f_diabetes)
    age_p = 0
    gen_p = 0
    dia_p = 0
    bp_p = 0
    ex_p = 0
    bmi_p = 0
    w_dia_p = 0
    # print 'diaaaaaaaaaaaaaa', type(weight), type(height)
    bmi = weight / ((((height) * (0.025)) ** 2))
    # print bmi
    w_age = {0: range(0, 40), 1: range(40, 50), 2: range(50, 60)}
    # m_bmi={0: (range(0,24 )), 1: (range(24,29 )), 2: range((29, 39))}
    for age_points, age_range in w_age.iteritems():
        if age in age_range:
            age_p = age_points
        else:
            if age > 60:
                age_p = 3
    # print age_p
    if f_diabetes == 'Yes':
        w_dia_p = 1
    else:
        w_dia_p = 0
    if bmi < 24:
        bmi_p = 0
    elif bmi >= 24 and bmi < 29:
        bmi_p = 1
    elif bmi >= 29 and bmi < 39:
        bmi_p = 2
    else:
        bmi_p = 3
    # print bmi_p

    if diabetes == 'Yes':
        dia_p = 1
    else:
        dia_p = 0
    # print dia_p
    if hypertension == 'Yes':
        bp_p = 1
    else:
        bp_p = 0
    # print bp_p
    if exercise == 'Yes':
        ex_p = 0
    else:
        ex_p = 1
    # print ex_p
    print age_p ,'age', bmi_p,'bmi', dia_p ,'dia', bp_p ,'hyper', ex_p ,'exer', gen_p,'gen',w_dia_p,'w dia'

    return age_p + bmi_p + dia_p + bp_p + ex_p + gen_p + w_dia_p

    def correct_bmr(h_feet,h_inch,weight):
        print('s')

# def connector():
#     if packs(age,gender,weight,height,smoker,diabetes,hypertension,exercise):
#         age,gender,weight,height,smoker,diabetes,hypertension,exercise=packs(age,gender,weight,height,smoker,diabetes,hypertension,exercise)
#         age,gender,weight,height,diabetes,hypertension,exercise=age,gender,weight,height,diabetes,hypertension,exercise
#     else:
#         age,weight,height,waists,workouts,diabetes_family,hypertensions,bg,eatsrisk(age,weight,height,waists,workouts,diabetes_family,hypertensions,bg,eats)
#         age,weight,height,diabetes,hypertension,exercise=age,weight,height,diabetes_family,hypertensions,workouts
#     return age,gender,weight,height,diabetes,hypertension,exercise




