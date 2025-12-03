from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import connection


@login_required 
def CaseManagerMain(request):
    return render(request, 'scrCaseManagerMain.html')
@login_required
def CaseManagerTable(request):
    return render(request,'scrCaseManagerTable.html')
@login_required
def CaseManagerView(request):
    return render(request, 'scrCaseManagerView.html')
