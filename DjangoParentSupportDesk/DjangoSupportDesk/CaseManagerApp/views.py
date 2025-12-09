from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection as conn


@login_required 
def CaseManagerMain(request):
    return render(request, 'scrCaseManagerMain.html')
@login_required
def CaseManagerTable(request):
      with conn.cursor() as cursor:
        cursor.execute(
            '''SELECT Case_ID as case_id, Title as title, Description as description, 
                      Category as category, Urgency as urgency, Status as status, 
                      Created_at as created_at
             FROM Case_Model 
             WHERE User_ID = %s
             ORDER BY Created_at DESC
             ''', [request.user.id] 
            )
        columns = [col[0] for col in cursor.description]
        cases = [dict(zip(columns, row))for row in cursor.fetchall()]

        return render(request,'scrCaseManagerTable.html', {'cases': cases})
      
@login_required
def CaseManagerView(request, case_id):
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM GetCase(%s)',
            [case_id]
        )
        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()

        if row:
            case = dict(zip(columns, row))
            if case['user_id'] != request.user.id:
                case = None
        else:   
            case = None
            
    return render(request, 'scrCaseManagerView.html', {'case': case})

@login_required 
def CaseManagerUpdateCase(request, case_id):
    if request.method == 'POST':
        newstat = request.POST['status']    
        appointment_date = request.POST['Appointment_date']
        if not appointment_date :
            appointment_date = None
        if not newstat:
            newstat = None

        with conn.cursor() as cursor:
            cursor.execute(
                'Select * from UpdateCase(%s,%s,%s)'
                , [case_id,newstat,appointment_date]
            )
            result = cursor.fetchone()
            if result[1]:
                    messages.success(request, result[2])
                    return redirect('scrCaseManagerView',case_id=case_id)
            else:
                    messages.error(request, result[2])
        return redirect('scrCaseManagerView', case_id=case_id)
        
    
