from django.urls import path 
from . import views 

urlpatterns = [
    path('scrSettings/', views.Settings, name='scrSettings'),
    path('scrNewCase/', views.NewCase, name='scrNewCase')
]