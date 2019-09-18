from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^products-for-professionals/$',)
    #url(r'^input/$', views.input, name='input'),
    url(r'^$', views.index, name='index'),
    #url(r'^about_us/$',views.about_us,name='about_us'),
    url(r'^loginpage/$',views.loginpage12,name='loginpage'),
    #url(r'^contact/$',views.contact,name='contact'),
    url(r'^login/$',views.loged,name='loged'),
    url(r'^resetpassword/$',views.resetpasswordview,name='firstreset'),
    url(r'^resend/$',views.resendpasswordview.as_view(),name='resend'),
    url(r'^resendpassword/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.resendview,name='resendpass'),
    url(r'^contct/$',views.contcter,name='contcter'),
    url(r'^trouble-signin/$', views.trouble, name='trouble'),
    url(r'^logout/$',views.logout_view,name='logout_view'),
    url(r'^reset-success/$', views.resetsuccessview, name='success'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^reset-password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.reset, name='reset'),
    url(r'^reset/$',views.resetview1.as_view(),name='reset'),
    url(r'^reset/(?P<id>[0-9]+)/$',views.resetview.as_view(),name='reset'),
    url(r'^userlogin/$',views.LoginView.as_view() ,name='login'), 
]