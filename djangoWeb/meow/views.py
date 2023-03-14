from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("MEOW MOTHATRUCKER")
def bonk(request):
    return HttpResponse("bonk")
def greet(request,name):
    return HttpResponse(f"Hello,{name}")
