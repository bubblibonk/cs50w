from django.shortcuts import render
import datetime

def index(request):
    now=datetime.datetime.now()
    return render(request,"newyear/index.html",{
        "newmeow":now.month == 1 and now.day == 1 
        })
