from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    #dboard_violation_review
    path('ViolationReportsActive', views.ViolationReportsActive, name='ViolationReportsActive'),
    path('ViolationReportsWarning', views.ViolationReportsWarning, name='ViolationReportsWarning'),
    path('ViolationReportsProbation', views.ViolationReportsProbation, name='ViolationReportsProbation'),
    path('ViolationReportsSuspension', views.ViolationReportsSuspension, name='ViolationReportsSuspension'),
    path('ViolationReportsExpulsion', views.ViolationReportsExpulsion, name='ViolationReportsExpulsion'),
    path('ViolationReportsInactive', views.ViolationReportsInactive, name='ViolationReportsInactive'),
    
    #issue_status
    path('IssueWarning', views.IssueWarning, name='IssueWarning'),
    path('IssueProbation', views.IssueProbation, name='IssueProbation'),
    path('IssueSuspension', views.IssueSuspension, name='IssueSuspension'),
    path('IssueExpulsion', views.IssueExpulsion, name='IssueExpulsion'),
    path('DenyReport', views.DenyReport, name='DenyReport'),
    
    #summary_report
    path('SummaryWarning', views.SummaryWarning, name='SummaryWarning'),
    path('SummaryProbation', views.SummaryProbation, name='SummaryProbation'),
    path('SummarySuspension', views.SummarySuspension, name='SummarySuspension'),
    path('SummaryExpulsion', views.SummaryExpulsion, name='SummaryExpulsion'), 
    
    #modify_status
    path('ModifyExpulsion', views.ModifyExpulsion, name='ModifyExpulsion'),
    path('ModifySuspension', views.ModifySuspension, name='ModifySuspension'),
    
    #dboard_modify_violation
    path('ModifyViolation', views.ModifyViolation, name='ModifyViolation'),
    path('Infopopup2', views.Infopopup2, name='Infopopup2'),
    path('AddViolation', views.AddViolation, name='AddViolation'),
    path('EditViolation', views.EditViolation, name='EditViolation'),
    
    #
    path('studrec/', views.studrec, name='studrec'),
    path('studrec2/', views.studrec2, name='studrec2'),
    path("studlist/", views.studlist, name="studlist"),
    path("studlist2/", views.studlist2, name="studlist2"),
    path("addlist/", views.addlist, name="addlist"),
    path("editlist/", views.editlist, name="editlist"),
    path("addcourse/", views.addcourse, name="addcourse"),
    path("editcourse/", views.editcourse, name="editcourse"),
    path("userrole/", views.userrole, name="userrole"),
    path("edituserrole/", views.edituserrole, name="edituserrole"),
    path("adduserrole/", views.adduser, name="adduserrole"),
    path("useraccount/",views.useraccount, name="useraccount"),
]