from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# ------ Student Records ------
def dashboard(request):
    return render(request,'Dashboard.html')
def studrec(request):
    return render(request, 'Student Records.html')
def studrec2(request):
    return render(request, 'Student Records 2.html')
def studlist(request):
    return render(request, 'Student List.html')
def studlist2(request):
    return render(request, 'Student List 2.html')
def addcourse(request):
    return render(request, 'addcourse.html')
def editcourse(request):
    return render(request, 'editcourse.html')
def editlist(request):
    return render(request, 'Editlist.html')
def addlist(request):
    return render(request, 'Addlist.html')    
# ------ User Roles ------
def userrole(request):
    return render(request, 'Account List.html') 
def edituserrole(request):
    return render(request, 'Edit User Role.html')
def adduser(request):
    return render(request, 'Add User.html')
def useraccount(request):
    return render(request, 'UserAccount.html')
