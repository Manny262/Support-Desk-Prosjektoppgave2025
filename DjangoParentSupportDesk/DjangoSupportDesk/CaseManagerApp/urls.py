from django.urls import path 
from . import views

urlpatterns = [
    path('CaseManagerMain/', views.CaseManagerMain, name='scrCaseManagerMain'),
    path('CaseManagerTable/', views.CaseManagerTable, name='scrCaseManagerTable'),
    path('CaseManagerView/', views.CaseManagerView, name='scrCaseManagerView')
]