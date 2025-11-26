from django.urls import path
from . import views 

urlpatterns = [
    path('scrUserMain/', views.UserMain, name='scrUserMain'),
    path('scrUserTable/', views.UserTable, name='scrUserTable'),
    path('scrUserView/', views.UserView, name='scrUserView')
]