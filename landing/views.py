# -*- coding: utf-8 -*-

from django.shortcuts import render

from landing.models import ListClient


def index(request):
    msg = False
    if request.method == 'POST' and request.POST.get('email') is not None:
        contact = ListClient(email=request.POST['email'])
        contact.save()
        msg = True
    return render(request, 'index.html', {'msg': msg})
