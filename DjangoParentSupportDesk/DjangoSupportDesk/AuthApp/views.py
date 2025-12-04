from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def scrLogin(request):
    return render(request, 'scrLogin.html')
def login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        
        user = authenticate(username=Username, password=Password)
        if user is not None:
            auth_login(request, user)
            if not request.user.is_staff:
                return redirect('scrUserMain')
            else:
                return redirect('scrCaseManagerMain')
        else:
            messages.error(request, 'Feil brukernavn eller passord')
    return render(request, 'scrLogin.html')


def scrRegister(request):
    return render(request, 'scrRegister.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1  = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(email=email, username=username, password=password1)
            user.save()
            messages.success(request, 'Bruker opprettet! Logg inn.')
            return render(request, 'scrRegister.html', {'redirect_after': True})
        else:
            messages.error(request, 'Passordene matcher ikke')
    return render(request, 'scrRegister.html')

@login_required 
def LogoutPage(request):
    logout(request)
    return redirect('scrLogin')
