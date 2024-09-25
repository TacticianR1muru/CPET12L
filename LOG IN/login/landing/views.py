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
