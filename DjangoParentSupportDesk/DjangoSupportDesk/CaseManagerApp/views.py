from django.shortcuts import render

# Create your views here.

def CaseManagerMain(request):
    return render(request, 'scrCaseManagerMain.html')

def CaseManagerTable(request):
    return render(request,'scrCaseManagerTable.html')

def CaseManagerView(request):
    return render(request, 'scrCaseManagerView.html')

