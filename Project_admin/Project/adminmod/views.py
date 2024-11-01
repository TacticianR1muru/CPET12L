from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .forms import SignupNow, ReportForm, ViolationTypeForm, UserForm, DenyReportForm
from .models import DropdownOption, Signup, Course, Section, Report, ViolationType, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
import string

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
def violationreports(request):
    return render(request, 'violationreports.html')
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
    if request.method == 'POST':
        form = DenyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or desired URL
    else:
        form = DenyReportForm()
    return render(request, 'dboard_violation_rev/issue_status/DenyReport.html',{'form': form})

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

import random
import string
from django.shortcuts import render
from .forms import UserForm
from .models import User

def generate_random_password(length=10):
    """Utility function to generate a random password."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def adduser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Generate email based on first and last name
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = f"{last_name.lower()}.{first_name.lower()}@email.com" if last_name else f"{first_name.lower()}@email.com"
            
            # Generate a random password
            password = generate_random_password()

            # Set the generated email and password on the form instance
            user = form.save(commit=False)
            user.email = email
            user.password = password  # Note: Normally, you'd hash the password before saving
            
            user.save()

            # Pass generated email and password to the template
            return render(request, 'user_role/Add User.html', {
                'form': form,
                'generated_email': email,
                'generated_password': password
            })
        else:
            # Return the form with errors if it's not valid
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

#def signup(request):
    #if request.method == "POST":
        #form = SignupNow(request.POST)
        #form.save()
        #return redirect("/")
    #else:
        #form = SignupNow()
    #return render(request, 'login/Sign-up.html', {"form": form})

#################################

def signup(request):
    if request.method == "POST":
        form = SignupNow(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Ensure you create this page or change this to your homepage

    else:
        form = SignupNow()

    return render(request,'login/Sign-up.html', {'form': form})


def manage_dropdown(request):
    if request.method == 'POST':
        # Add a new program
        if 'add_program' in request.POST:
            new_program = request.POST.get('new_program')
            if new_program:
                DropdownOption.objects.create(program1=new_program)
                return redirect('manage_dropdown')

        # Add a new course
        if 'add_course' in request.POST:
            new_course = request.POST.get('new_course')
            program_id = request.POST.get('program_id')
            if new_course and program_id:
                program = DropdownOption.objects.get(id=program_id)
                Course.objects.create(program=program, course_name=new_course)
                return redirect('manage_dropdown')

        # Add a new section
        if 'add_section' in request.POST:
            new_section = request.POST.get('new_section')
            course_id = request.POST.get('course_id')
            if new_section and course_id:
                course = Course.objects.get(id=course_id)
                Section.objects.create(course=course, section_name=new_section)
                return redirect('manage_dropdown')

        # Delete a program
        if 'delete_program' in request.POST:
            program_id = request.POST.get('delete_program')
            DropdownOption.objects.filter(id=program_id).delete()
            return redirect('manage_dropdown')

        # Delete a course
        if 'delete_course' in request.POST:
            course_id = request.POST.get('delete_course')
            Course.objects.filter(id=course_id).delete()
            return redirect('manage_dropdown')

        # Delete a section
        if 'delete_section' in request.POST:
            section_id = request.POST.get('delete_section')
            Section.objects.filter(id=section_id).delete()
            return redirect('manage_dropdown')

    # Fetch all options for the dropdowns
    program_options = DropdownOption.objects.all()
    course_options = Course.objects.all()
    section_options = Section.objects.all()

    return render(request, 'manage_dropdown.html', {
        'program_options': program_options,
        'course_options': course_options,
        'section_options': section_options,
    })

# Report filing view for Guards
def file_report(request):
    if request.method == 'POST':
        # Get form data directly from POST
        student_id = request.POST.get('student')
        incident_date = request.POST.get('incident_date')
        violation_type_id = request.POST.get('violation_type')
        
        try:
            # Get the related objects
            student = Signup.objects.get(id=student_id)
            violation_type = ViolationType.objects.get(id=violation_type_id)
            
            # Prepare data for summary
            context = {
                'student_id': student.idnumber,
                'student_name': f"{student.first_name} {student.last_name}",
                'incident_date': incident_date,
                'violation_type': violation_type.name,
                # Store IDs for database insertion
                'db_student_id': student_id,
                'db_violation_type_id': violation_type_id
            }
            return render(request, 'report_summary.html', context)
        except (Signup.DoesNotExist, ViolationType.DoesNotExist) as e:
            return HttpResponse(f"Error: {str(e)}", status=400)

    # GET request - show the form
    violation_types = ViolationType.objects.all()
    students = Signup.objects.all()
    return render(request, 'file_report.html', {
        'violation_types': violation_types,
        'students': students
    })

def deny_report(request, report_id):
    # Retrieve the report instance by its ID
    report = get_object_or_404(Report, id=report_id)
    
    # Pass the report details to the template
    context = {
        'student_id': report.student.idnumber,
        'student_name': f"{report.student.first_name} {report.student.last_name}",
        'incident_date': report.incident_date,
        'violation_type': report.violation_type.name,
    }
    return render(request, 'denyreport.html', context)


def report_summary(request):
    if request.method == 'POST':
        if 'confirm_submission' in request.POST:
            try:
                # Create and save the report
                report = Report.objects.create(
                    student_id=request.POST.get('db_student_id'),
                    incident_date=request.POST.get('incident_date'),
                    violation_type_id=request.POST.get('db_violation_type_id')
                )
                return redirect('report_success')
            except Exception as e:
                return HttpResponse(f"Error saving report: {str(e)}", status=500)
        
        elif 'cancel_submission' in request.POST:
            return redirect('file_report')
    
    return redirect('file_report')

def report_success(request):
    return render(request, 'report_success.html')

# Manage Violations (for admins)
def manage_violations(request):
    violations = ViolationType.objects.all()
    if request.method == 'POST':
        form = ViolationTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_violations')
    else:
        form = ViolationTypeForm()

    return render(request, 'manage_violations.html', {'form': form, 'violations': violations})

# Edit Violation
def edit_violation(request, violation_id):
    violation = ViolationType.objects.get(id=violation_id)
    if request.method == 'POST':
        form = ViolationTypeForm(request.POST, instance=violation)
        if form.is_valid():
            form.save()
            return redirect('manage_violations')
    else:
        form = ViolationTypeForm(instance=violation)

    return render(request, 'edit_violation.html', {'form': form, 'violation': violation})



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


def registration_success(request):
    return render(request, 'registration_success.html')

def report_success(request):
    return render(request, 'report_success.html')