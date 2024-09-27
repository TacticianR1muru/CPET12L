from django.urls import  path

from . import views

urlpatterns = [
    path('addstudent', views.addstudent, name='addstudent'),
    path('notif', views.notif, name='notif'),
    path('reportsummary', views.reportsummary, name='reportsummary'),
    path('guardsearch',  views.guardsearch, name='guardsearch'),
    path('guardsearch2',   views.guardsearch2, name='guardsearch2'),
]