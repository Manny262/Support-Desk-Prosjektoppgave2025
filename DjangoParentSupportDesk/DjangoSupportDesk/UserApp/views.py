from django.shortcuts import render

# Create your views here.
def UserMain(request):
    return render(request, 'scrUserMain.html')

def UserTable(request):
    return render(request, 'scrUserTable.html')

def UserView(request):
    return render(request, 'scrUserView.html')