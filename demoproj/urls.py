"""demoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
url(r'^', include('beforelogin.urls',namespace='before_l')),
url(r'^', include('foodandacti.urls',namespace='foodandacti')),
url(r'^', include('healthandrecords.urls',namespace='healthandrecords')),
url(r'^', include('insuranceandcygen.urls',namespace='insuranceandcygen')),
url(r'^', include('apiforapp.urls',namespace='apiforapp')),
url(r'^', include('usermanagement.urls',namespace='usermanagement')),
#url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
#url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

] 

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)