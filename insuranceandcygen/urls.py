from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^in/insurance_packs/(?P<slug>[\w-]+)/$', views.indiinsurance, name='indiinsurance'),
    url(r'^in/insurance_packs/$', views.infoindiinsurance, name='infoindiinsurance'),
]