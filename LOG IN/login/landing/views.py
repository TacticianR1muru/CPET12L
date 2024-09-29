from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'LOGIN.html')

def signup(request):
    return render(request, 'Sign-up.html')

def reset(request):
    return render(request, 'Reset Password.html')

def resetconfirmation(request):
    return render(request, 'Reset Password Confirmation.html')

def forget(request):
    return render(request, 'Forget Password.html')

def change(request):
    return render(request, 'ForceChange.html')

def code(request):
    return render(request, 'Enter Code.html')
