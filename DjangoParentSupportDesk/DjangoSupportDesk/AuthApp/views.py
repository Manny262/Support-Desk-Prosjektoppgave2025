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
        else:
            messages.error(request, 'Feil brukernavn eller passord')
            return render(request, 'scrLogin')


def scrRegister(request):
    return render(request, 'scrRegister.html')

def register(request):
    if request.method == 'Post':
        email = request.POST['email']
        username = request.POST['username']
        password1  = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(email=email, username=username, password=password1)
            user.save()
            print('User created')
            return redirect('scrLogin')

def LogoutPage(request):
    return render(request, 'scrLogoutPage.html')
