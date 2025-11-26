from django.shortcuts import render

# Create your views here.
def scrLogin(request):
    return render(request, 'scrLogin.html')
def login(request):
    print("hei")


def scrRegister(request):
    return render(request, 'scrRegister.html')

def register(request):
    print('hei')

def LogoutPage(request):
    return render(request, 'scrLogoutPage.html')