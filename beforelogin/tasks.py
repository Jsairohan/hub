from __future__ import absolute_import, unicode_literals

from demoproj.celeryproj import app
# from celerytest.celery import celery_app
# from celery import Celery
from celery.schedules import crontab
from django.core.mail import send_mail,send_mass_mail
import requests
import json
from beforelogin.models import User
# from healthandrecords.models import Risk_sore
from datetime import date#datetime.date.today
import datetime
from django.db.models import Sum
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from foodandacti.models import usersfoodsdairy,setgoalsd,activitysecduled
# from phase_1.profileupdates.heathandacti import bulkhealthtipsemail
import random
# app = Celery()

# @celery_app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     # sender.add_periodic_task(
#     #     crontab(hour=7, minute=30, day_of_week=1),
#     #     test.s('Happy Mondays!'),
#     # )

# payload = { "sender": "SOCKET", "route": "4", "country": "91",
# "sms": [
# { "message": "Message2", "to": [str(mobilenumber) ] } ] }
# payload=json.dumps(payload)
# headers = {
# 'authkey': "225056A39bSLPXl5b434284",
# 'content-type': "application/json"
# }
# r = requests.post("http://api.msg91.com/api/v2/sendsms", data = payload,headers=headers)
# print r.status_code
@app.task(queue='diet_tasks',ignore_result=True)
def send_bulkdeittonormalusertipsemail():
    deitgoal = Foodfornormal.objects.all()
    todate = date.today().strftime("%Y-%m-%d")
    ids = Risk_sore.objects.values_list('user_id',flat=True)
    deitgoal = Foodfornormal.objects.all()
    deitgoalbreakids = deitgoal.filter(Breakfast='yes').values_list('id',flat=True)
    deitgoalluchids = deitgoal.filter(Lunch='yes').values_list('id', flat=True)
    deitgoaldinnerids = deitgoal.filter(Dinner='yes').values_list('id', flat=True)

    # print ids
    sender='mailauthentication@cygengroup.com'
    usedeatils = User.objects.all()
    for id in ids:
        print id

        beakfast=deitgoal.get(id=random.choice(deitgoalbreakids)).name
        lunch = deitgoal.get(id=random.choice(deitgoalluchids)).name
        dinner = deitgoal.get(id=random.choice(deitgoaldinnerids)).name
        # convars=bulkhealthtipsemail(id)
        # print  convars.get('food'),   convars.get('activities'), convars.get('goal'),usedeatils.filter(id=id).last().first_name
        contentmessage = render_to_string('before_login/lowriskuserdiet', {
            'username': usedeatils.filter(id=id).last().first_name,
            'domain': 'https://www.cygengroup.com',
            'todate':todate,
            'breakfast': beakfast,
            'lunch':lunch,
            'dinner':dinner,

        })

        send_mail(
            'foods Review',
            contentmessage,
            sender,
            [usedeatils.filter(id=id).last().email],
            fail_silently=True,
        )
        print 'crossedd content message here after here',usedeatils.filter(id=id).last().first_name,usedeatils.filter(id=id).last().email
        payload = {"sender": "SOCKET", "route": "4", "country": "91",
                   "sms": [
                       {"message": str(contentmessage), "to": [str(usedeatils.filter(id=id).last().phone)]}]}

        payload = json.dumps(payload)
        print payload
        headers = {
            'authkey': "228180AyXSxlFg935b586ff0",
            'content-type': "application/json"
        }
        r = requests.post("http://api.msg91.com/api/v2/sendsms", data=payload, headers=headers)
        print r.status_code

@app.task(ignore_result=True,queue='balancediet_tasks')
def send_bulkhealthtipsemail(sender=None):
    ids = setgoalsd.objects.values_list('user_id',flat=True)
    print ids
    usedeatils = User.objects.all()
    sender = 'mailauthentication@cygengroup.com'
    if ids:
        for id in ids[:len(ids) - 1]:
            print id
            convars = bulkhealthtipsemail(id)
            # print  convars.get('food'),   convars.get('activities'), convars.get('goal'),usedeatils.filter(id=id).last().first_name
            contentmessage = render_to_string('before_login/smsfoodanddiet', {
                'username': usedeatils.filter(id=id).last().first_name,
                'domain': 'https://www.cygengroup.com',
                'food': convars.get('food'),
                'goal': convars.get('goal'),
                'activities': convars.get('activities'),
                'what': convars.get('what')
            })
            print 'crossedd content message here after here'
            send_mail(
                'Goal Review',
                contentmessage,
                sender,
                [usedeatils.filter(id=id).last().email],
                fail_silently=True,
            )

    else:
        pass

    # datatuple = [('subject3', 'content', 'manohar@cygengroup.com', [user.email]) for user i
    #              User.objects.all() if user.is_active]

    # send_mass_mail(datatuple, fail_silently=True)

        #, 'goaldddddddaaaaaaaaaay'
        # print activitysecduled.objects.filter(user_id=id).filter(dayofweek=newweekday).aggregate(Sum('calburnt'))

            # dailtgoal=context['dailtgoal'].calneeded-activitysecduled.objects.filter(user_id=id).filter(dayofweek=newweekday).aggregate(Sum('dayofweek'))
        # print context['dailtgoal'].calneeded
        # change_type
        #print context
# context['newdaily']=dailtgoal
@app.task()
def send_bulktipsemail():
    datatuple = [('subject3', 'content', 'manohar@cygengroup.com', [user.email]) for user in
                 User.objects.all() if user.is_active]

    send_mass_mail(datatuple, fail_silently=True)



@app.task()
def send_verification_email(subject=None,contentmessage=None,sender=None,reciver=None):
    send_mail(
        subject,
        contentmessage,
        sender,
        reciver,
        fail_silently=True,
    )
    print reciver

@app.task()
def send_restpassword_email(subject=None,contentmessage=None,sender=None,reciver=None):
    send_mail(
        subject,
        contentmessage,
        sender,
        reciver,
        fail_silently=True,
    )

@app.task()
def send_restsussuss_email(subject=None,contentmessage=None,sender=None,reciver=None):
    send_mail(
        subject,
        contentmessage,
        sender,
        reciver,
        fail_silently=True,
    )


@app.task()
def send_wellcom_email(subject=None,contentmessage=None,sender=None,reciver=None):
    send_mail(
        subject,
        contentmessage,
        sender,
        reciver,
        fail_silently=True,
    )

@app.task()
def send_wellcom_sms(mobilenumber=None,subject=None):
    print mobilenumber
    payload = {"sender": "CYGENH", "route": "4", "country": "91",
              "sms": [
              { "message": subject, "to": [str(mobilenumber) ] } ] }
    print mobilenumber
    payload=json.dumps(payload)
    headers = {
              'authkey': "228180AyXSxlFg935b586ff0",
              'content-type': "application/json"
              }
    requests.post("http://api.msg91.com/api/v2/sendsms", data = payload,headers=headers)
    


@app.task
def add(x,y):
    # send_mail(
    #     'Subject here12',
    #     'Here is the message12.',
    #     x,
    #     [y],
    #     fail_silently=False,
    # )
    print(x+y)

@app.task()
def send_password_email(subject=None,contentmessage=None,sender=None,reciver=None):
    send_mail(
        subject,
        contentmessage,
        sender,
        reciver,
        fail_silently=True,
)


@app.task()
def send_password_sms(mobilenumber=None, subject=None):
    payload = {"sender": "CYGENH", "route": "4", "country": "91",
               "sms": [
                   {"message": subject, "to": [str(mobilenumber)]}]}

    payload = json.dumps(payload)
    headers = {
        'authkey': "228180AyXSxlFg935b586ff0",
        'content-type': "application/json"
    }
    requests.post("http://api.msg91.com/api/v2/sendsms", data=payload, headers=headers)