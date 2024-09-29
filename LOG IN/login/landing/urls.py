from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('reset', views.reset, name='reset'),
    path('resetconfirmation', views.resetconfirmation, name='resetconfirmation'),
    path('forget', views.forget, name='forget'),
    path('change', views.change, name='change'),
    path('code', views.code, name='code'),
]