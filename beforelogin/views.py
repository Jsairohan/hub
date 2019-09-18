# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .forms import Loginform,Registerform,ContactForm
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate,logout
from django.core.cache import cache
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib import messages
from django.template.loader import get_template
from  beforelogin.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from rest_framework.views import APIView
from usermanagement.models import *
from django.shortcuts import get_object_or_404
import json
import random
from django.utils import timezone
import string
from beforelogin.tasks import send_verification_email,send_restpassword_email,send_wellcom_email,send_restsussuss_email,send_wellcom_sms,send_bulkhealthtipsemail,send_password_email,send_password_sms



# Create your views here.


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

det = {'Vitamins_details': '', 'Cardiac_details':'' ,
               'Dietary_details':'' ,
               'Family_medical_details':'' ,
               'Confidential_details': '',
               'Past_medical_details':'' ,
               'Smoking_details':'' ,
               'health_details': '', 'person_details':'',
               'demo_details':'' , 'alchoal_details': '',"risk_score":'','profile_details':''}



class Geter_cache:
    def __init__(self,user="user",iteam=None,user_speci=None,id=None,tables=None,updater=None,user_dic=None,updater_value=None):
        self.user=user
        self.iteam=iteam
        self.user_speci=user_speci
        self.id=id
        self.tables=tables
        self.updater = updater
        self.user_dic=user_dic
        self.updater_value=updater_value
        print updater_value,'updater_value',user_speci,'user_speci'
    def common_cache(self):
        # try:
        user_person = cache.get(self.id)
        print user_person,'user_person'
        if user_person:
            common_details = cache.get(self.id)
            print common_details,'theses arw common details'
            return common_details
        else:

            cache.set(self.id,  det, 180 * 60)
            common_details = cache.get(self.id)
            return common_details


    def users_cache_speci(self):
        if not self.user_dic:
            self.user_dic={}
            self.user_dic[self.user_speci]=''
            # self.user_dic =user_speci
            # print self.user_dic,'user dic',self.user_speci

        # try:
        specific_details = self.user_dic.get(self.user_speci)
        # print 'specific_details',specific_details
        #
        if not specific_details:
            aa = cache.get(self.id)
            # print aa,'aaaaaaaaaaaaaaaaaaaaaaaaaa'
            if not aa:
                aa = {}
                aa[self.user_speci] = get_or_none(self.tables, user_id=self.id)
                cache.set(self.id, aa, 180 * 60)
                specific_details = cache.get(self.id).get(self.user_speci)
                print "before caching the caching aa", specific_details
                return specific_details
            else:
                aa[self.user_speci] = get_or_none(self.tables, user_id=self.id)
                cache.set(self.id, aa, 180 * 60)
                specific_details = cache.get(self.id).get(self.user_speci)
                print "before caching the caching after aa", specific_details
                return specific_details
        #     else:
        return specific_details
        #
        # except:
        #     #specific_details=
        #     #self.user_dic[self.user_speci]=specific_details
        #     aa = cache.get(self.id)
        #     if not aa:
        #         aa={}
        #         aa[self.user_speci] = get_or_none(self.tables, user_id=self.id)
        #         cache.set(self.id, aa, 180 * 60)
        #         specific_details = cache.get(self.id).get(self.user_speci)
        #         print "before caching the caching aa",specific_details
        #         return specific_details
        #     else:
        #         aa[self.user_speci] = get_or_none(self.tables, user_id=self.id)
        #         cache.set(self.id, aa, 180 * 60)
        #         specific_details = cache.get(self.id).get(self.user_speci)
        #         print "before caching the caching after aa",specific_details
        #         return specific_details

    def users_cache_updater(self):

        aa=cache.get(self.id)
        if aa:
            pass
        else:
            aa={}
        cache.delete(self.id)

        aa[self.user_speci] = self.updater_value

        cache.set(self.id, aa, 180 * 60)
        common_details = cache.get(self.id)

        common_details=common_details.get(self.user_speci)

        #common_details = cache.get("user").get().get()

        return common_details

def validate_username(request):
    email = request.GET.get('email', None)
    phone = request.GET.get('phone', None)
    data={}
    if email:
        data = {
        'is_taken': User.objects.filter(email__iexact=email).exists(),
        'is_phonetaken': User.objects.filter(phone=phone).exists()
    }
        if data['is_taken']:
            data['error_message'] = 'A user with this email already exists.'
    elif phone:
        data = {

            'is_phonetaken': User.objects.filter(phone=phone).exists()
        }
        if data['is_phonetaken']:
            data['errorphone_message'] = 'A user with this mobile number already exists.'

    return JsonResponse(data)


def index(request):
    #return HttpResponse('yourayhome')
    #return render(request, 'personal_health/parameter.html')
    # cache.clear()
    return render(request, 'before_login/newhome.html')

def trouble(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = get_or_none(User, email=email)
        if user:
            name = user.first_name
            current_site = get_current_site(request)
            mail_subject = 'Reset your Password.'
            message = render_to_string('reset_active.html', {
                'user': name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user)
            })
            send_mail(
                mail_subject,
                message,
                'mailauthentication@cygengroup.com',
                [user.email],
                fail_silently=True
            )
            return render(request, 'forgotpassword_link.html')
    return render(request, 'before_login/trouble_signin.html')


def reset(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        userid = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        userid = None
    if userid is not None and account_activation_token.check_token(userid, token):
        if request.method == "POST":
            new_password = request.POST.get("newpassword")
            con_password = request.POST.get("confirmpassword")
            if new_password == con_password:
                userid.password = make_password(new_password)
            else:
                return HttpResponse('Password dont match')
            userid.save()
            return render(request, 'Password_change_Success.html')
        return render(request, 'before_login/forgot_password.html')
    else:
        return HttpResponse('Password Reset link is invalid!')



def contcter(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            return HttpResponse('data posted')

    form = ContactForm()
    print form.is_bound()
    return render(request, 'form1.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user_id = request.user.id
                reset_password=request.user.is_reset
		branch_code = Staff.objects.filter(staff_id=user_id)[0].branch_code
                org_code = branch_code.split('-')[0]
                return Response({"Code":1,"Message":"Login Succsessfull","Sessionid": user_id,"reset_password":reset_password,"Organisation code":org_code,"Branch code":branch_code},status=status.HTTP_200_OK)
            else:
                return Response({"Code":-1,"Message":"Invalid Login"},status=status.HTTP_200_OK)
        else:
            return Response({"Code":-1,"Message":"Invalid Login"},status=status.HTTP_200_OK)


def loged(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass_word = request.POST.get("password")
        # user = authenticate(email=email, password=pass_word)
        # if user is not None:
        #     if user.is_active:
        #         from django.forms.models import model_to_dict
        #
        #
        #         #request.session.set_expiry(86400)  # sets the exp. value of the session
        #
        #
        #         login(request, user)
        #         request.session["userid"] = user.id
        try:
            user = authenticate(email=email, password=pass_word)

            if user is None:
                messages.warning(request, 'Details are not matching')
                return redirect('/loginpage/')

        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        user = User.objects.get(email=email)

        if user.is_superuser == True:
            pass
        else:
            pro = Profile.objects.get(user=user)
            expire_pass = timezone.timedelta(days=3) + pro.reset_time
            # print user.reset_time
            print expire_pass
            if pro.reset_time > expire_pass and user.is_reset == True:
                print user.is_reset, 'before'
                user.is_reset = True
                print user.is_reset, 'after'
                return redirect('/resendpassword/' + email + '/')

        if user is not None:
            if user.is_active:
                from django.forms.models import model_to_dict

                # request.session.set_expiry(86400)  # sets the exp. value of the session

                login(request, user)
                request.session["userid"] = user.id
                user_verify = request.user.is_reset
                print user_verify, 'shdfkh'
                if user_verify == True:
                    print 'dshhgh'
                    return redirect('/resetpassword/')
                if user.is_superuser == True:
                    return redirect('/admindashboard/')
                else:
		    if pro.user_type.id == 1:
                        return redirect('/admindashboard/')
                    if pro.user_type.id == 2:
                        return HttpResponse('<h1 style="color:red">nurse dashboard</h1>')
                    if pro.user_type.id == 3:
                        # return redirect('/un_treated_patients_list/')
                        return redirect('/doctordashboard/')
                    if pro.user_type.id == 4:
                        return redirect('/healthassement/')
                    if pro.user_type.id == 6:
                        return redirect('/hrdashboard/')

                a = Geter_cache(id=user.id).common_cache()
                request.session["first_name"] = user.first_name
                a = request.GET.get('next')
                # print a,'ddddddddddddddddddddddddddddddddddddddddddddddddd'
                if a:
                    return redirect(a)
                print 'i am healthassement', a

            else:
                messages.warning(request,
                                 'Verfication is incomplete hence complete account verification {}'.format(user.email))
                return redirect('/')
        else:
            # if
            # user = get_or_none(User, email=email)
            messages.warning(request, 'Details are not matching')
            return redirect('/')
    return render(request, 'before_login/newhome.html')


# changes june8

def resetpasswordview(request):
    return render(request, 'before_login/reset1.html')


class resendpasswordview(views.APIView):
    def post(self, request, **kwargs):

        Email = request.data.get('email')
        print Email
        #password = make_password(password)
        u = User.objects.get(email = Email)
        characters = string.ascii_letters + string.digits
        pasrd = "".join(random.choice(characters) for x in range(8))
        print pasrd
        pswd = make_password(pasrd)
        u.password = pswd
        u.reset_time = timezone.now()
        print u.reset_time
        mail_subject = "SUCCESSFUL REGISTRATION"
        contentmessage = render_to_string('before_login/verification_email2', {
            'user': u.first_name,
            'email': u.email,
            'userpassword': pasrd,
        })
        send_password_email.apply_async(kwargs={'subject': mail_subject, 'contentmessage': contentmessage,
                                                'sender': 'mailauthentication@cygengroup.com',
                                                'reciver': [u.email]}, queue='passwordemail')

        #send_password_sms.apply_async(
         #   kwargs={
          #      'subject': 'Dear {0} ,your password has expired your new credintials,Your email is {1}.Your login password for Aimhealth is {2} (password change is mandatory upon first login)'.format(
           #         u, u.email, pasrd),
            #    'mobilenumber': u.phone},
            #queue='passwordsms')
        u.save()
        if u:
            return Response({"sucess": "password sent"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"success": "incorrect username"}, status=status.HTTP_204_NO_CONTENT)


def resendview(request,email):
    return render(request, 'before_login/resend.html', {'email':email})

def resetsuccessview(request):
    return render(request, 'Password_change_Success.html')

def loginpage12(request):
    return render(request, 'before_login/loginpage.html')

class resetview1(APIView):
    def post(self, request, **kwargs):
        password = request.data.get('password')
        print password
        #password = make_password(password)
        u = User.objects.get(id = request.user.id)
        print u
        u.password=make_password(password)
        u.is_reset = False
        u.save()
        if u:
            return Response({"sucess": "changed password"}, status=status.HTTP_200_OK)
        else:
            return Response({"success": "incorrect password"}, status=status.HTTP_204_NO_CONTENT)


class resetview(APIView):
    def post(self, request,id, **kwargs):
        password = request.data.get('password')
        #password = make_password(password)
        u = get_object_or_404(User,id=id)
        if u and password:
            print u
            u.password = make_password(password)
            u.is_reset = False
            u.save()
            return Response({"Message":"changed password","code": 1,"Sessionid" :u.id}, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"improper password","code": -1}, status=400)