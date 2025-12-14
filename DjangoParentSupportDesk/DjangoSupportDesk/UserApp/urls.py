from django.urls import path
from . import views 

urlpatterns = [
    path('scrUserMain/', views.UserMain, name='scrUserMain'),
    path('scrUserTable/', views.UserTable, name='scrUserTable'),
    path('scrUserView/<int:case_id>/', views.UserView, name='scrUserView'),
    path('UserNewComment/<int:case_id>/<str:bool_param>/', views.UserNewComment, name='UserNewComment')
]