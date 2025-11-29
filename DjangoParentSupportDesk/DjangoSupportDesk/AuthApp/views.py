from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def scrLogin(request):
    return render(request, 'scrLogin.html')
def login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['passsword']
        
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('scrCaseManagerMain')
    


def scrRegister(request):
    return render(request, 'scrRegister.html')

def register(request):
    print('hei')

def LogoutPage(request):
    return render(request, 'scrLogoutPage.html')