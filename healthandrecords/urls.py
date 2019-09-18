from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^healthassement/$', views.health_ana, name='health_ana'),
    url(r'^preventivemeasures/$',views.pre_meas , name='pre_meas'),
    url(r'^cygenpacks/$', views.Cyegn_packs,name='cygenpacks'),
    url(r'^hopspital_packes/$', views.Hosptila_packs,name='hospital_pack'),
    url(r'^profile_form/$', views.evaluation_form_view_details,name='first_form'),
    url(r'^profile_form/refill/$', views.evaluation_form_view_details_editer,name='first_formediter'),
    url(r'^today_hel/$', views.today_hel,name='today_hel'),
]