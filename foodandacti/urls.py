from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^createactivity/(?P<slug>[\w-]+)/$',views.UserActivityscheduleCreate.as_view(),name='createactivity'),
    url(r'^creategoal/$', views.SetgoalCreate.as_view(), name='creategoal'),
    url(r'^userinfopost/$', views.usersummarypostview.as_view(), name='userinfopost'),
    url(r'^summary/$', views.completesummaryview.as_view(), name='summary'),
    url(r'^medicalinfopost/$', views.mediclummarypostview.as_view(), name='medicalinfopost'),
    url(r'^createacti/$',views.Activityredirct,name='activityredirct'),
    url(r'^fooddairy/update/$', views.personal_info_update.as_view(),name='personal_info_update'),
    url(r'^foodnew/$', views.foodform1, name='editss'),
    url(r'^foodnew/(?P<pk>\d+)/$', views.foodform, name='edits'),
    url(r'^profile/$', views.personal_info, name='profile'),
    url(r'^fooddetails/search/$',views.fooddetails_search, name='fooddetails_search'),
    url(r'^fooddairy/recordupdate/(?P<pk>\d+)/$',views.foodupdateview, name='foodupdate'),
    url(r'^fooddairy/delete/(?P<pk>\d+)/$',views.fooddeleteview, name='fooddelete'),
    url(r'^createactivity/update/(?P<pk>\d+)/$',views.activiesupdateview, name='activityupdate'),
    # url(r'^dietandactivites/$',views.foodactivityview, name='fooddetails_activites'),

]