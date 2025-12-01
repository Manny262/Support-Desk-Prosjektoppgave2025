from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrLogin, name='scrLogin'),
    path('login/', views.login, name='login'),
    path('scrRegister/', views.scrRegister, name='scrRegister'),
    path('register/', views.register, name='register'),
    path('scrLogoutPage/', views.LogoutPage, name='scrLogoutPage')

    ]


