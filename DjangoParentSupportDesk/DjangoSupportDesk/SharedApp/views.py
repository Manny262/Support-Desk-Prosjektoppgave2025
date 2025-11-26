from django.shortcuts import render

# Create your views here.
def Settings(request):
    return render(request, 'scrSettings.html')

def NewCase(request):
    return render(request, 'scrNewCase.html')