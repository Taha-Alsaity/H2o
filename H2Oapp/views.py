from django.shortcuts import render
from django.shortcuts import render
from .models import stats,calstats
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login , logout , get_user_model
from django.contrib import messages
# Create your views here.
from datetime import datetime
# Create your views here.



def mainindex(request):
    
    

    return  render(request,'index/mainpage.html',{
    
    })

def indexC(request):
    stat = calstats.objects.get(id=1)
    

    return  render(request,'index/indexC.html',{
    'stat': stat
    })

def indexCen(request):
    stat = calstats.objects.get(id=1)
    

    return  render(request,'index/indexCen.html',{
    'stat': stat
    })

def index(request):
    stat = stats.objects.get(id=1)
    

    return  render(request,'index/index.html',{
    'stat': stat
    })
def indexen(request):
    stat = stats.objects.get(id=1)
    

    return  render(request,'index/indexen.html',{
    'stat': stat
    })

def calc(request ,name):
    if request.method == 'POST':
        stat = stats.objects.get(id=1)
    
        weight = request.POST['weight']
        age = request.POST['age']
        hegiht = request.POST['tall']
        active = request.POST['active']
        weight = int(weight) * 2.2046
        water = int(weight) / 2
        water = (int(water) + ((int(active)/30) * 12)) * 0.02957
        stat.number += 1
        stat.save()
        messages.success(request,f'{round(water, 2)}')
    return  redirect(f'{name}')



def calcalc(request ,name):
    if request.method == 'POST':
        stat = calstats.objects.get(id=1)
    
        weight = request.POST['weight']
        age = request.POST['age']
        hegiht = request.POST['tall']
        active = request.POST['active']
        gender = request.POST['gender']
        if(gender == "male"):
           calo = 10 * int(weight)  + 6.25 * int(hegiht)  - 5 * int(age) + 5

        elif(gender == "female"):
           calo =  10 * int(weight)  + 6.25 * int(hegiht)  - 5 * int(age) - 161
        
        calo = calo * float(active)
        stat.number += 1
        stat.save()
        messages.success(request,f'{round(calo, 2)}')
    return  redirect(f'{name}')

