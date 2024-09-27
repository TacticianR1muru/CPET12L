from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('studrec/', views.studrec, name='studrec'),
    path('studrec2/', views.studrec, name='studrec2'),
    path("studlist/", views.studlist, name="studlist"),
    path("studlist2/", views.studlist2, name="studlist2"),
    path("addcourse/", views.addcourse, name="addcourse"),
    path("editcourse/", views.editcourse, name="editcourse"),
]
