from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
# Create your views here.
@login_required
def Settings(request):
    return render(request, 'scrSettings.html')
@login_required
def NewCase(request):
    return render(request, 'scrNewCase.html')

@login_required
def CreateCase(request):
    if request.method == 'POST': 
        inpTitle = request.POST.get('title')
        inpDescription = request.POST.get('description')
        inpCategory = request.POST.get('category')
        inpUrgency = request.POST.get('urgency')
        inpUserID = request.user.id

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    'Select * from NewCase(%s, %s, %s,%s, %s, %s)',
                    [inpTitle, inpDescription, inpCategory, inpUrgency,'pending', inpUserID]
                )

                result = cursor.fetchone()

                if result[1]:
                    messages.success(request, result[2])
                    match request.user.is_staff:
                        case True:
                            return redirect('scrCaseManagerMain')
                        case False: 
                            return redirect('scrUserMain')
                else:
                    messages.error(request, result[2])

        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        return render(request, 'scrNewCase.html')

