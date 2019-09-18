# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decko import dash_compleletd
from .models import *
from django.core.cache import cache
# Create your views here.

@login_required(login_url="/login/")
@dash_compleletd
def indiinsurance(request,slug):
    plans = cache.get('indiplans')

    if not plans:
        plans1 = Indian_insur.objects.all()
        cache.set('plans', plans1, 180*60)
        plans = cache.get('plans')
    context=plans.get(urls=slug)

    return render(request,'navbar/indiinsurance.html',{'context':context})

@login_required(login_url="/login/")
@dash_compleletd
def infoindiinsurance(request):
    insurance1 = []
    insurance2 = []

    # id = request.session["userid"]

    plans = cache.get('indiplans')

    if not plans:
        plans1 = Indian_insur.objects.all()
        cache.set('plans', plans1, 180*60)
        plans = cache.get('plans')
    for i in range(len(plans)):
        if i % 2 != 0:
            insurance1.append(plans[i])
        else:
            insurance2.append(plans[i])

    c = {'insurance1': insurance1, 'insurance2': insurance2}
    return render(request, 'navbar/insurbase.html', c)
