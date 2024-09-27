from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
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