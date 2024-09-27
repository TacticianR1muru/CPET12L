from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')
def studrec(request):
    return render(request, 'Student Records.html')
def studrec2(request):
    return render(request, 'Student Records2.html')
def studlist(request):
    return render(request, 'Student List.html')
def studlist2(request):
    return render(request, 'Student List 2.html')
def addcourse(request):
    return render(request, 'Student-Records-add-course.html')
def editcourse(request):
    return render(request, 'Student-Records-edit-course.html')