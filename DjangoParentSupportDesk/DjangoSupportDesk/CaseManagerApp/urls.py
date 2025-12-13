from django.urls import path 
from . import views

urlpatterns = [
    path('CaseManagerMain/', views.CaseManagerMain, name='scrCaseManagerMain'),
    path('CaseManagerTable/', views.CaseManagerTable, name='scrCaseManagerTable'),
    path('CaseManagerTableAll/', views.CaseManagerTableAll, name='scrCaseManagerTableAll'),
    path('CaseManagerView/<int:case_id>/', views.CaseManagerView, name='scrCaseManagerView'),
    path('CaseManagerUpdateCase/<int:case_id>/', views.CaseManagerUpdateCase, name='CaseManagerUpdateCase'),
    path('CaseManagerNewComment/<int:case_id>/<str:bool_param>/', views.CaseManagerNewComment, name='CaseManagerNewComment'),
]