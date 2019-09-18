def hyperdiaplay(val):
    # print val,'hyperdiaplay'
    # print val,"hyper tenstion"
    if  val > 3 and val<=5:
        lev='High'
        levtext='''Since you are on the higher side of hypertension problems You fall into the secondary recommendation stage for preventive measures. it is advised primarily that if you are suffering from obstructive sleep apnoea which is a sleep disorder of having episodes of obstructive sleep you should get it checked. It has a high contributing risk factor for hypertension, Few of the
        recommendation that is advised so that higher bp can be prevented are in the following: Stress shouldbe reduced considerably and strategies like relaxing music to doing moderate workouts are to be practised daily Unhealthy eating, drugs, smoking, alcohol intake and other means of such activities are to be avoided because they add upto  more hypertensive problems Long term hypertension risks can prove a bad effect on heart and give rise to cardiovascular problems hence bp to be monitored and kept in check regularl
        y'''
        return lev, levtext
    elif  val== 3:
        lev = 'Moderate'
        levtext='''The greatest long term potential for avoiding hypertension is to apply prevention strategies early in life.To not let oneself be exposed to high hypertension problems and be wary of his or her own health you need to have bp monitored regularly, Since you fall in the primary recommendation stage of the hypertension problem we advise you to keep a healthy diet plan which otherwise can lead to dizziness, fainting dehydration and other serious medical problems.Aerobic movements, with brisk walking, limiting alcohol use and DASH eating plans are part of the primary preventive measures in hypertension Untreated hypertension can lead to serious complications like brain stroke, kidney failure, congestive heart failure and retinal problems'''
        return lev, levtext
    elif  val >= 0 and  val < 3:
        lev = 'Low'
        levtext=''' Some consider complete prevention of hypertension to be impossible. Blood pressure tends to rise with age in all modern cultures.But populations leading a primitive lifestyle with high physical activity, low calorie intake and diet high in potassium low in sodium intake do not have an age associated rise in blood pressure.Adopting health policies in the primordial stages at an early age would likely reduce hypertension and its correlated cardiovascular problems.'''
        return lev,levtext
    elif  val >5:
        return 'Diagnosed',''
    else :
        return None,''



def diabdiaplay(val):
    # print val, 'diabdiaplay'
    if  val > 5 and val<=10:
        lev='High'
        levtext='''Falling under the secondary tier of recommendation and preventive measure list  it is advised primarily that physical exercises should be practised regularly as 30 minutes to 2.5 hours of physical activity can lower your diabetes risk by 7% and can cut down the risk into half. Secondary prevention is based on the earliest possible identification of diabetes evidence based intervention. Hence blood tests should be done in 3-6 months so that a proper screening can be done and blood glucose levels are lowered in diabetic patients with proper nutrition plan'''
        return lev, levtext
    elif  val== 5:
        lev = 'Moderate'
        levtext='''The low score of diabetes does not indicate no risk . As a primordial assessment of diabetes you should be aware of your lifestyle and also cautioned about family members since diabetes has been linked to genetic reasons hence a moderate nutrition plan and diabetes related blood tests should be done in 6-12 months and blood glucose levels are to be monitored effectively '''
        return lev, levtext
    elif  val >= 0 and  val <= 5:
        lev = 'Low'
        levtext='''  Since your diabetes score is moderately low you should further on follow the optimal levels of five modifiable risk factors(normal weight, no smoking, regular physical activity and low risk dietary score and moderate alcohol consumption) Falling under the primary category lifestyle intervention has been proved to be most effective since an effective diabetic nutrition plan, restricted calorie intake is recommended at this stage which are the mainstay of primary prevention of diabetes. Also limiting and cutting down on smoking, alcohol intake can lower the risk of diabetes. Avoidance of obesity is the major primary preventive measure for diabetes'''
        return lev,levtext
    elif  val >10:
        return 'Diagnosed', ''
    else :
        return None,''

def obesitybdiaplay(val,etinicity):
    # print val, 'obesitybdiaplay'
    if etinicity == "Non-Asian":
        if  val <= 18.59:
            lev = 'Underweight'
            levtext=''' Since you fall in the low category of preventive measures therefore you are at less risk of developing obesity. This means that preventive measures is needed that can inhibit the emergence of risk factors for obesity and cultural patterns, behavioral conditions can be altered depending on the risk factors.In primordial prevention efforts should be encouraged such that you do not get yourself prone to harmful lifestyle such as:1.High alcoholic consumption and extensively smoking 2.Over eating and leading sedentary lifestyle with no physical activities '''
        elif  val >= 18.60 and  val <= 24.99:
            lev = 'Normal'
            levtext='''Having a moderately low risk of obesity does not rule out entirely that you will not be susceptible to the risk of obesity at all. It means since you fall under the primary preventive measures you should focus on a healthy lifestyle behavior related to maintaining a normal weight, practising good nutrition and having regular physical activity The primary prevention is targeted to reduce the likelihood of the disease. BMI are to be checked very carefully and screening for the purpose of overweight and obesity should be monitored '''
        elif  val >= 25 and  val <= 29.99:
            lev = 'Overweight'
            levtext='''Having a moderately low risk of obesity does not rule out entirely that you will not be susceptible to the risk of obesity at all. It means since you fall under the primary preventive measures you should focus on a healthy lifestyle behavior related to maintaining a normal weight, practising good nutrition and having regular physical activity The primary prevention is targeted to reduce the likelihood of the disease. BMI are to be checked very carefully and screening for the purpose of overweight and obesity should be monitored '''
        else:
            lev = 'Obese'
            levtext = '''Since you have a higher risk of developing obesity you fall into the secondary recommendation of the preventive measures and these following recommendations should be followed in order to maintain a health life with less risk factors of obesity The waist circumference in adults are used to provide an estimate of adipose tissue accumulation hence it should be in check and any abnormal conditions should be furthermore investigatedHealthy diet with proper nutrition plan and avoiding skipping of meals are to be avoided Intake of less unhealthy foods with strictly avoiding alcohol usage improving sleep and reducing stress '''
        # print lev,levtext
        return lev,levtext
    else:
        if val <= 18.5:
            lev = 'Underweight'
            levtext = ''' Since you fall in the low category of preventive measures therefore you are at less risk of developing obesity. This means that preventive measures is needed that can inhibit the emergence of risk factors for obesity and cultural patterns, behavioral conditions can be altered depending on the risk factors.In primordial prevention efforts should be encouraged such that you do not get yourself prone to harmful lifestyle such as:1.High alcoholic consumption and extensively smoking 2.Over eating and leading sedentary lifestyle with no physical activities '''
        elif val >= 18.5 and val <= 22.99:
            lev = 'Normal'
            levtext = '''Having a moderately low risk of obesity does not rule out entirely that you will not be susceptible to the risk of obesity at all. It means since you fall under the primary preventive measures you should focus on a healthy lifestyle behavior related to maintaining a normal weight, practising good nutrition and having regular physical activity The primary prevention is targeted to reduce the likelihood of the disease. BMI are to be checked very carefully and screening for the purpose of overweight and obesity should be monitored '''
        elif val >= 23 and val <= 24.99:
            lev = 'Overweight'
            levtext = '''Having a moderately low risk of obesity does not rule out entirely that you will not be susceptible to the risk of obesity at all. It means since you fall under the primary preventive measures you should focus on a healthy lifestyle behavior related to maintaining a normal weight, practising good nutrition and having regular physical activity The primary prevention is targeted to reduce the likelihood of the disease. BMI are to be checked very carefully and screening for the purpose of overweight and obesity should be monitored '''
        elif val >= 25 and val <= 29.99:
            lev = 'Pre-Obese'
            levtext = '''Having a moderately low risk of obesity does not rule out entirely that you will not be susceptible to the risk of obesity at all. It means since you fall under the primary preventive measures you should focus on a healthy lifestyle behavior related to maintaining a normal weight, practising good nutrition and having regular physical activity The primary prevention is targeted to reduce the likelihood of the disease. BMI are to be checked very carefully and screening for the purpose of overweight and obesity should be monitored '''
        else:
            lev = 'Obese'
            levtext = '''Since you have a higher risk of developing obesity you fall into the secondary recommendation of the preventive measures and these following recommendations should be followed in order to maintain a health life with less risk factors of obesity The waist circumference in adults are used to provide an estimate of adipose tissue accumulation hence it should be in check and any abnormal conditions should be furthermore investigatedHealthy diet with proper nutrition plan and avoiding skipping of meals are to be avoided Intake of less unhealthy foods with strictly avoiding alcohol usage improving sleep and reducing stress '''

        # print lev,levtext
        return lev, levtext


def heartdiaplay(val,gender):
    # print val, 'heartdiaplay'
    # if gender=='Male':

    if gender == 'Male':
        if val <= 5:
            lev = 'Low'
            levtext = '''Although cardiovascular events are less likely to occur in people with low levels of risk, no level of risk can be considered safe Since you fall into the low categorical sector for cardiac problems therefore primordial care for cardiac problems is needed. Low risk does not mean no risk Conservative management such as:Good healthy habits No smoking and alcohol consumption Daily physical activities should be practised For individuals in low risk categories, they can have a health impact at lower cost compared to individual counselling and therapeutic approaches.'''
            return lev, levtext
        elif val >= 6 and val <= 11:
            lev = 'Moderate'
            levtext = '''Since you are at moderately low percentage of the 
 problems therefore you fall into the primary recommendation sector. Individuals in this category are at moderate risk of fatal or nonfatal vascular events. The primary preventive measure includes:Monitor your cardiovascular risk profile every 6-12 months.So before the onset of cardiovascular disease its is mandatory to see that lifestyle factors such food and nutrition are balanced, behaviors of smoking and alcohol are to be avoided and risk factors to be aware of'''
            return lev, levtext
        elif val >= 12 and val <= 20:
            lev = 'High'
            levtext = '''Since you fall into the secondary tier of recommendation it means that individuals in this category are at high risk of fatal or nonfatal vascular events. Since it is for long term ,the symptoms and illness are considered chronic therefore the goal is to achieve an improved quality of life and lengthen overall life expectancy by preventing further complications in future by working out and having a healthy meal plan. Hence risk profile should be monitored every 3-6 months.In the context of this the secondary recommendation it is advised the following: early screening, detection and determining family history and risk factors are to be stratergized because its is aimed both at controlling risk factors and also have therapeutic approaches such as: 1.The risk problems with all the related cardiovascular diseases such as heart attack or stroke prevention of recurrence of the problems are to be avoided.  2.Purpose designed exercise programs 3. Health education and counselling  and Support of self management should be practised'''
            return lev, levtext
        elif val >20:
            return 'Diagnosed',''
        else :
            return None,''
    else:
        if val <= 13:
            lev = 'Low'
            levtext = '''Although cardiovascular events are less likely to occur in people with low levels of risk, no level of risk can be considered safe Since you fall into the low categorical sector for cardiac problems therefore primordial care for cardiac problems is needed. Low risk does not mean no risk Conservative management such as:Good healthy habits No smoking and alcohol consumption Daily physical activities should be practised For individuals in low risk categories, they can have a health impact at lower cost compared to individual counselling and therapeutic approaches.'''
            return lev, levtext
        elif val > 14 and val <= 19:
            lev = 'Moderate'
            levtext = '''Since you are at moderately low percentage of the cardiac problems therefore you fall into the primary recommendation sector. Individuals in this category are at moderate risk of fatal or nonfatal vascular events. The primary preventive measure includes:Monitor your cardiovascular risk profile every 6-12 months.So before the onset of cardiovascular disease its is mandatory to see that lifestyle factors such food and nutrition are balanced, behaviors of smoking and alcohol are to be avoided and risk factors to be aware of'''
            return lev, levtext
        elif val >= 20 and val<28:
            lev = 'High'
            levtext = '''Since you fall into the secondary tier of recommendation it means that individuals in this category are at high risk of fatal or nonfatal vascular events. Since it is for long term ,the symptoms and illness are considered chronic therefore the goal is to achieve an improved quality of life and lengthen overall life expectancy by preventing further complications in future by working out and having a healthy meal plan. Hence risk profile should be monitored every 3-6 months.In the context of this the secondary recommendation it is advised the following: early screening, detection and determining family history and risk factors are to be stratergized because its is aimed both at controlling risk factors and also have therapeutic approaches such as: 1.The risk problems with all the related cardiovascular diseases such as heart attack or stroke prevention of recurrence of the problems are to be avoided.  2.Purpose designed exercise programs 3. Health education and counselling  and Support of self management should be practised'''
            return lev, levtext
        elif val >= 28:
            return 'Diagnosed', ''
        else:
            return None,''

# email='suhas.cygengroup@gmail.com'
# passowrd='Suhas@123'
# a,b=hyperdiaplay(4)
# print a,b
# c,d=diabdiaplay(6)
# print c,d