#bmr
#BMR = 370 + (21.6 x LBM) - LBM = lean body mass in Kg
# lean body mass in Kg


class Bmr():
    def __init__(self,gender=None,height=None,weight=None,age=None):
        self.gender=gender
        self.height=height
        self.weight=weight
        self.age=age
    def women_bmr(self):
        bmr=655.0955 + (9.5634* self.weight)+(1.8496 * self.height )-(4.6756*self.age)
        #bmr=10 * self.weight+(6.25*self.height)-(5 * self.age)  -161
        return bmr*1.2
    def men_bmr(self):
        bmr = 66.4730+ (13.7516 * self.weight) + (5.0033 * self.height) - (6.7550 * self.age)
        #bmr=10 * self.weight+(6.25*self.height)-5 * self.age +5

        #print bmr
        return bmr*1.2

#calries in take
class Claries():
    def __int__(self,activity=None,time=None,target=None,target_time=None,gender=None,height=None,weight=None,age=None):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.activity=activity
        self.time=time/30.0
        self.target=target*7700
        self.target_time=target_time



    def cal_men_gian(self):
        #7,700 Kcal
        self.bmr = 66.4730 + (13.7516 * self.weight) + (5.0033 * self.height) - (6.7550 * self.age)

        gain=self.bmr-(self.activity*self.time)+((self.target*7700)/float(self.target_time))+ (self.activity * self.time)
        # print self.weight,self.height,self.age,"cal_men_gian",self.bmr,gain,self.target,self.target_time
        return gain
    def cal_women(self):
        self.wbmr = 655.0955 + (9.5634 * self.weight) + (1.8496 * self.height) - (4.6756 * self.age)
        gain = self.wbmr-(self.activity*self.time)+((self.target*7700)/float(self.target_time))+ (self.activity * self.time)
        return gain
    def cal_men_loss(self):
        #7,700 Kcal
        self.bmr = 66.4730 + (13.7516 * self.weight) + (5.0033 * self.height) - (6.7550 * self.age)
        loss=self.bmr-(self.activity*self.time)+((self.target*7700)/float(self.target_time))
        return loss
    def cal_women_loss(self):
        self.wbmr = 655.0955 + (9.5634 * self.weight) + (1.8496 * self.height) - (4.6756 * self.age)
        loss = self.wbmr-(self.activity*self.time)+((self.target*7700)/float(self.target_time))
        return loss
    def cal_men_main(self):
        self.bmr = 66.4730 + (13.7516 * self.weight) + (5.0033 * self.height) - (6.7550 * self.age)
        #7,700 Kcal
        loss = self.bmr + (self.activity * self.time)
        return loss
    def cal_women_main(self):
        self.wbmr = 655.0955 + (9.5634 * self.weight) + (1.8496 * self.height) - (4.6756 * self.age)
        loss = self.wbmr+(self.activity*self.time)
        return loss

#class nutri():

# a=[90,100,110,120,130,140,150,160,170,180,190,200,220,240,260,280,300]
# b=[]
# for i in a:
#     b.append('kg_'+str(int(round(0.453592*i))))
#
# print b


#body fat per

class Bfp:
    def __init__(self, Total_body_weight=None, Wrist_measurement_full=None,Waist_measurement_naval=None,
                 Hip_measurement_fullest=None,Forearm_measurement_fullest=None):
        self.Total_body_weight=Total_body_weight
        self.Wrist_measurement_full=Wrist_measurement_full
        self.Waist_measurement_naval=Waist_measurement_naval
        self.Hip_measurement_fullest=Hip_measurement_fullest
        self.Forearm_measurement_fullest=Forearm_measurement_fullest

        def women_bfp(self):
            Factor_1 = (self.Total_body_weight * 0.732) + 8.987
            Factor_2 = self.Wrist_measurement_full / 3.140
            Factor_3 = self.Waist_measurement_naval * 0.157
            Factor_4 = self.Hip_measurement_fullest * 0.249
            Factor_5 = self.Forearm_measurement_fullest * 0.434
            lbm = Factor_1 + Factor_2 - Factor_3 - Factor_4 + Factor_5
            bfw = Total_body_weight - lbm
            bpgc = (bfw * 100) / Total_body_weight
            return bpgc
        def men_bfp():
            Factor_1 = (self.Total_body_weight * 1.082) + 94.42
            Factor_2 = self.Wrist_measurement_full * 4.15
            lbm = Factor_1 - Factor_2
            bfw = Total_body_weight - lbm
            bpgc = (bfw * 100) / Total_body_weight
            return bpgc
#
#
# c=Claries()
#
# c.height = 176.784
# c.weight =70
# c.age = 24
# c.activity=55
# c.time=45/30.0
# c.target=2*7700
# c.target_time=10
# c.bmr = 66.4730 + (13.7516 * c.weight) + (5.0033 * c.height) - (6.7550 * c.age)
# d=c.bmr
# b=c.cal_men_gian()
# print b,d
#
