from django.urls import path

from . import views

urlpatterns = [
    path('infopopup',  views.infopop, name='infopopup'),
    path('monitorreport'  , views.monitorrep, name='monitorreport'),
    path('reportsummarystudent'   , views.reportsumstud, name='reportsummarystudent'),
    path('studentsettings'    , views.studset, name='studentsettings'),
    path('studentstatus'     , views.studstat, name='studentstatus'),

]
