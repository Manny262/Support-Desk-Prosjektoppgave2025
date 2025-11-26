from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrLogin, name='scrLogin'),
    path('', views.login, name='login'),
    path('register/', views.scrRegister, name='scrRegister'),
    path('register/', views.register, name='register'),
    path('scrLogoutPage/', views.LogoutPage, name='scrLogoutPage')

    ]


