from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required 
def UserMain(request):
    return render(request, 'scrUserMain.html')
@login_required 
def UserTable(request):
    return render(request, 'scrUserTable.html')
@login_required 
def UserView(request):
    return render(request, 'scrUserView.html')