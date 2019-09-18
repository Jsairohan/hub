from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # superadmin
    url(r'^admins/$', views.getAdminListview.as_view(), name='admins'),
    url(r'^adminlist/$',views.adminlistview, name='admin'),

    #Create api's
    url(r'^staff/$', views.Createstaffview.as_view(), name='registration'),
    url(r'^admin/$', views.Createadmin.as_view(), name='adminregister'),
    url(r'^patient/$', views.Createpatient.as_view(), name='patientregister'),
    url(r'^distributor/$', views.Createorgid.as_view(), name='orgid'),
    url(r'^branch/$', views.Createbranchid.as_view(), name='brnachid'),
    url(r'^corporate/$',views.Createcorporatebranchid.as_view(),name='corpbranhc'),
    url(r'^corporatehr/$',views.Createcorporatehrid.as_view(),name='corphr'),#staff/

    #get api's
    url(r'^doctors/$', views.get_Physician_listview.as_view(), name='doctors'),
    url(r'^nurses/$', views.get_Nurse_listview.as_view(), name='nurses'),
    url(r'^medtechs/$', views.get_MedTech_listview.as_view(), name='medtechs'),
    url(r'^corporatehrs/$',views.get_corp_hr.as_view(), name='corporatehrs'),
    url(r'^distributors/$', views.getorgid.as_view(), name='distributors'),
    url(r'^branches/$', views.get_Branches_listview.as_view(), name='branches'),
    url(r'^corporates/$', views.get_corp_listview.as_view(), name='corporates'),
    url(r'^patients/$', views.get_patients_doctor.as_view(), name='patients'),

    #get update delete api's
    url(r'^admin/(?P<user_id>[0-9]+)/$', views.Rud_admin_details_view.as_view(), name='deleteadmin'),
    url(r'^staff/(?P<staff_id>[0-9]+)/$', views.Rud_doctor_details_view.as_view(), name='updatedoctor'),
    url(r'^corporatehr/(?P<hr_id>[0-9]+)/$', views.Rud_corphr_details_view.as_view(), name='updatedoctor'),
    url(r'^patient/(?P<patient_code>[0-9]+)/$', views.link_patient_view.as_view()),
    #url(r'^rud_staff_details/(?P<staff_id>[0-9]+)/$', views.Rud_doctor_details_view.as_view(), name='updatedoctor'),

    #templateviews
    url(r'^admindashboard/$',views.adminview, name='admindashboard'),
    url(r'^doctorlist/$',views.doctorview, name='doctor'),
    url(r'^nurselist/$',views.nurseview, name='nurse'),
    url(r'^medtechlist/$',views.medtechview, name='medtech'),
    url(r'^corporatehrlist/$',views.corporatehr_view, name='medtech'),
    url(r'^distributerlist/$',views.organizationview, name='organization'),
    url(r'^branchlist/$',views.branchview, name='branch'),
    url(r'^corporatebranchlist/$',views.corporate_branchview, name='corp'),
    url(r'^profile/(?P<staff_id>[0-9]+)/$', views.staff_profile_view, name='doctorProfile'),
    url(r'^corporatehrprofile/(?P<hr_id>[0-9]+)/$', views.CorpHR_profile_view, name='doctorProfile'),
    # Doctor
    url(r'^doctordashboard/$',views.doctordashboardview, name='doctordashboard'),
    url(r'^treatedpatientslist/$',views.treatedpatientsview, name='treatedpatients'),
    url(r'^untreatedpatientslist/$',views.nontreatedpatientsview, name='nontreatedpatients'),#
    url(r'^patientsummary/(?P<pat_id>[0-9]+)/$',views.patientsummary, name='patientsummaryindoctor'),
    url(r'^medication/$',views.savemedication.as_view(), name='savemedicationforpatient'),#savethearapicrpatient

    url(r'^suggestion/$', views.doctorPresciption.as_view(), name='doctorsuggetion'),
    url(r'^thearapicsuggestion/$', views.savethearapicrpatient.as_view(), name='savethearapicrpatient'),

    #CorporateHR
    url(r'^hrdashboard/$',views.hrdashboard_view, name='hrdashboard'),
    url(r'^(?P<path>[a-z]+)patients/$',views.corporatepatientsview, name='corporatepatients'),
    url(r'summary/(?P<pat_id>[0-9]+)/$',views.patientsummary, name='patientslist_in_corporate_hr_dashboard'),
    # patienthealthanalysisinHR
    url(r'^healthanalysis(?P<analysis>[a-zA-Z]+)/$',views.patienthealthanalysisinHR, name='patienthealthanalysisinHR'),
    # Other
    # url(r'^getphysiciansfornurse/(?P<patient_code>[0-9]+)/$', views.get_doctors_patient.as_view()),

    # url(r'^getstaffProfile/(?P<staff_id>[0-9]+)/$', views.getstaffProfile.as_view(), name='StaffProfile'),
    # url(r'^patientcops/$', views.get_Patients_listview.as_view(), name='Patients'),

    #
    
    # url(r'doctordashboard/$',views.doctordashboardview, name='doctordashboard'),
   
    

]
urlpatterns = format_suffix_patterns(urlpatterns)