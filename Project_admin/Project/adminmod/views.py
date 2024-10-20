from django.shortcuts import render
from django.shortcuts import HttpResponse
import random
import string
from .forms import UserForm
from .models import User
from django.http import JsonResponse

# Create your views here.

# ------ Admin Dashboard ------
def dashboard(request):
    return render(request,'Dashboard.html')
# ------ Violation Review ------
#dboard_violations
def SummaryActive(request):
    return render(request, 'dboard_violation_rev/ReportSummary1.html')
def SummaryInactive(request):
    return render(request, 'dboard_violation_rev/ReportSummary2.html')
def ViolationReportsActive(request):
    return render(request, 'dboard_violation_rev/ViolationReportsActive.html')
def ViolationReportsWarning(request):
    return render(request, 'dboard_violation_rev/ViolationReportsWarning.html')
def ViolationReportsProbation(request):
    return render(request, 'dboard_violation_rev/ViolationReportsProbation.html')
def ViolationReportsSuspension(request):
    return render(request, 'dboard_violation_rev/ViolationReportsSuspension.html')
def ViolationReportsExpulsion(request):
    return render(request, 'dboard_violation_rev/ViolationReportsExpulsion.html')
def ViolationReportsInactive(request):
    return render(request, 'dboard_violation_rev/ViolationReportsInactive.html')

#issue_status dboard_violation_rev/issue_status/ 
def IssueWarning(request):
    return render(request, 'dboard_violation_rev/issue_status/IssueWarning.html')
def IssueProbation(request):
    return render(request, 'dboard_violation_rev/issue_status/IssueProbation.html')
def IssueSuspension(request):
    return render(request, 'dboard_violation_rev/issue_status/IssueSuspension.html')
def IssueExpulsion(request):
    return render(request, 'dboard_violation_rev/issue_status/IssueExpulsion.html')
def DenyReport(request):
    return render(request, 'dboard_violation_rev/issue_status/DenyReport.html')

#summary_report dboard_violation_rev/summary_report/
def SummaryWarning(request):
    return render(request, 'dboard_violation_rev/summary_report/SummaryWarning.html')
def SummaryProbation(request):
    return render(request, 'dboard_violation_rev/summary_report/SummaryProbation.html')
def SummarySuspension(request):
    return render(request, 'dboard_violation_rev/summary_report/SummarySuspension.html')
def SummaryExpulsion(request):
    return render(request, 'dboard_violation_rev/summary_report/SummaryExpulsion.html')
def SummaryActive(request):
    return render(request, 'dboard_violation_rev/summary_report/ReportSummary1.html')
def SummaryInactive(request):
    return render(request, 'dboard_violation_rev/summary_report/ReportSummary2.html')



#modify_stat dboard_violation_rev/summary_issue/
#modify_stat dboard_violation_rev/summary_issue/
def ModifyExpulsion(request):
    return render(request, 'dboard_violation_rev/modify_issue/ModifyExpulsion.html')
def ModifySuspension(request):
    return render(request, 'dboard_violation_rev/modify_issue/ModifySuspension.html')
def ModifyProbation(request):
    return render(request, 'dboard_violation_rev/modify_issue/ModifyProbation.html')
def ProbationProgress(request):
    return render(request, 'dboard_violation_rev/modify_issue/ProbationProgress.html')

# ------ Modify Violation ------
#dboard_modify
def ModifyViolation(request):
    return render(request, 'dboard_modify_violation/ModifyViolation.html')
def Infopopup2(request):
    return render(request, 'dboard_modify_violation/Infopopup2.html')
def AddViolation(request):
    return render(request, 'dboard_modify_violation/AddViolation.html')
def EditViolation(request):
    return render(request, 'dboard_modify_violation/EditViolation.html')

# ------ Student Records ------
def studrec(request):
    return render(request, 'studrec/Student Records.html')
def studrec2(request):
    return render(request, 'studrec/Student Records 2.html')
def studlist(request):
    return render(request, 'studrec/Student List.html')
def studlist2(request):
    return render(request, 'studrec/Student List 2.html')
def addcourse(request):
    return render(request, 'studrec/addcourse.html')
def editcourse(request):
    return render(request, 'studrec/editcourse.html')
def editlist(request):
    return render(request, 'studrec/Editlist.html')
def addlist(request):
    return render(request, 'studrec/Addlist.html')    
# ------ User Roles ------
def userrole(request):
    return render(request, 'user_role/Account List.html') 
def edituserrole(request):
    return render(request, 'user_role/Edit User Role.html')

def generate_random_password():
    # Function to generate a random password
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

def adduser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Process form data if valid
            employee_id = form.cleaned_data['employee_id']
            employee_name = form.cleaned_data['employee_name']
            position = form.cleaned_data['position']

            try:
                first_name, last_name = employee_name.split(' ')
            except ValueError:
                # Handle cases where there isn't a proper "First Last" format
                first_name, last_name = employee_name, ""

            # Generate email based on first and last name
            email = f"{last_name.lower()}.{first_name.lower()}@email.com" if last_name else f"{first_name.lower()}@email.com"
            
            password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

            # Create user
            user = User.objects.create(
                employee_id=employee_id,
                employee_name=employee_name,
                email=email,
                password=password,
                position=position,
            )
            
            # Pass generated email and password to the template
            return render(request, 'user_role/Add User.html', {
                'form': form,
                'generated_email': email,
                'generated_password': password
            })
        else:
            return render(request, 'user_role/Add User.html', {'form': form})

    # Generate a random password for the initial GET request
    password = generate_random_password()
    return render(request, 'user_role/Add User.html', {
        'form': UserForm(),
        'generated_password': password
    })

# View for generating a new password via AJAX
def retry_password(request):
    if request.method == 'GET':
        new_password = generate_random_password()
        return JsonResponse({'generated_password': new_password})

    # If GET request or form is invalid, re-render the empty form
    #return render(request, 'user_role/Add User.html', {'form': UserForm()})






def useraccount(request):
    return render(request, 'user_role/UserAccount.html')
#------ Login ------
def login(request):
    return render(request, 'login/LOGIN.html')

def signup(request):
    return render(request, 'login/Sign-up.html')

def reset(request):
    return render(request, 'login/Reset Password.html')

def resetconfirmation(request):
    return render(request, 'login/Reset Password Confirmation.html')

def forget(request):
    return render(request, 'login/Forget Password.html')

def change(request):
    return render(request, 'login/ForceChange.html')

def code(request):
    return render(request, 'login/Enter Code.html')
#------ studentmod ------
def infopop(request):
    return render(request, 'studentmod/infopopup.html')

def monitorrep(request):
    return render(request, 'studentmod/MonitorReport.html')

def reportsumstud(request):
    return render(request, 'studentmod/ReportSummaryStudent.html')

def studset(request):
    return render(request, 'studentmod/Student Settings.html')

def studstat(request):
    return render(request, 'studentmod/Student Status.html')
def infopopup3(request):
    return render(request, 'studentmod/infopopup3.html')

#------- guard and instructor module ------
def  addstudent(request):
    return render(request, 'guard-instructormod/AddStud.html')

def guardsearch(request):
    return render(request, 'guard-instructormod/Guard Search.html')

def guardsearch2(request):
    return render(request, 'guard-instructormod/Guard Search 2.html')

def notif(request):
    return render(request, 'guard-instructormod/Guard Notification.html')

def reportsummary(request):
    return render(request, 'guard-instructormod/Guard Report Summary.html')
