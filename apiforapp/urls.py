from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^registration/$', csrf_exempt(views.Createpatientview.as_view())),
    url(r'^healthassesment/post/$', csrf_exempt((views.Createpatientevaluvationview.as_view()))),
    url(r'^healthassesment/get/(?P<patient_code>[0-9]+)/$', views.Getpatientevaluvationview.as_view()),
    url(r'^userinfo/post/$', csrf_exempt((views.Createpatientinformationview.as_view()))),
    url(r'^userinfo/get/(?P<patient_code>[0-9]+)/$', views.Getpatientinformationview.as_view()),
    url(r'^riskscore/get/(?P<patient_code>[0-9]+)/$', views.Getpatienteriskscoreview.as_view()),
    url(r'^risk/test/$',views.buhn),
    url(r'^getParam/test/$',views.paramcreateview.as_view()),
    url(r'^glucometer/post/$', csrf_exempt((views.Createglucosview.as_view()))),
    url(r'^oximeter/post/$', csrf_exempt((views.Createoximeterview.as_view()))),
    url(r'^temperature/post/$', csrf_exempt((views.CreateTemperatureview.as_view()))),
    url(r'^bpmmeter/post/$', csrf_exempt((views.CreateBpmmeterview.as_view()))),
    url(r'^weightmeter/post/$', csrf_exempt((views.CreateWeightmeterview.as_view()))),
    url(r'^spirometer/post/$', csrf_exempt((views.CreateSpirometeryview.as_view()))),
    url(r'^hb/post/$', csrf_exempt((views.Himobloginpostview.as_view()))),
    url(r'^hba1c/post/$', csrf_exempt((views.Hbacpostview.as_view()))),
    url(r'^ldl/post/$', csrf_exempt((views.Ldlpostview.as_view()))),
    url(r'^tcl/post/$', csrf_exempt((views.Totalcolestrolpostview.as_view()))),
    url(r'^tri/post/$', csrf_exempt((views.Triglecyridespostview.as_view()))),
    url(r'^hdl/post/$', csrf_exempt((views.Createhdlmeterview.as_view()))),
    url(r'^Urine/post/', csrf_exempt((views.Urinepostview.as_view()))),
    url(r'^ECG/post/$', csrf_exempt((views.ECGcreateview.as_view()))),
    url(r'^ecg/get/(?P<id>[0-9]+)$', csrf_exempt((views.ECGgetview.as_view()))),
    url(r'^ECG12lead/post/$', csrf_exempt((views.ECGNIGcreateview.as_view()))),
    url(r'^Eval/post/$', csrf_exempt((views.Evaluationcreateview.as_view()))),
    url(r'^Eval/get/$', csrf_exempt((views.Evaluationgetview.as_view()))),
    url(r'^media/(?P<path>.*)$',views.openfle),
    # url(r'^user/delete/(?P<patient_code>[0-9]+)$', csrf_exempt((views.Userdeleteview.as_view()))),
    # url(r'^userid/get/$', csrf_exempt((views.getuserids.as_view())))


]
urlpatterns = format_suffix_patterns(urlpatterns)