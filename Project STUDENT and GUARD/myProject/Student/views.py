from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def infopop(request):
    return render(request, 'infopopup.html')

def monitorrep(request):
    return render(request, 'MonitorReport.html')

def reportsumstud(request):
    return render(request, 'ReportSummaryStudent.html')

def studset(request):
    return render(request, 'Student Settings.html')

def studstat(request):
    return render(request, 'Student Status.html')