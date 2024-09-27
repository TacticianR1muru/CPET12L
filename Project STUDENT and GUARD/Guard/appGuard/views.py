from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def  addstudent(request):
    return render(request, 'AddStud.html')

def guardsearch(request):
    return render(request, 'Guard Search.html')

def guardsearch2(request):
    return render(request, 'Guard Search 2.html')

def notif(request):
    return render(request, 'Guard Notification.html')

def reportsummary(request):
    return render(request, 'Guard Report Summary.html')