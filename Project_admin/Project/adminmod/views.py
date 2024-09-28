from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

# ------ Admin Dashboard ------
def dashboard(request):
    return render(request,'Dashboard.html')
# ------ Violation Review ------
#dboard_violations
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

#modify_stat dboard_violation_rev/summary_issue/
def ModifyExpulsion(request):
    return render(request, 'dboard_violation_rev/summary_issue/ModifyExpulsion.html')
def ModifySuspension(request):
    return render(request, 'dboard_violation_rev/summary_issue/ModifySuspension.html')

# ------ Modify Violation ------
#dboard_modify
def ModifyViolation(request):
    return render(request, 'db_modify_violation/ModifyViolation.html')
def Infopopup2(request):
    return render(request, 'db_modify_violation/Infopopup2.html')
def AddViolation(request):
    return render(request, 'db_modify_violation/AddViolation.html')
def EditViolation(request):
    return render(request, 'db_modify_violation/EditViolation.html')

# ------ Student Records ------
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
