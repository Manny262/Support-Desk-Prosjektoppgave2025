from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection as conn
from django.contrib.auth.models import User

def getCaseManagerName(id):
    if id:
        return User.objects.get(id=id).username


@login_required 
def CaseManagerMain(request):
    return render(request,'scrCaseManagerMain.html', {'Name': getCaseManagerName(request.user.id)})
@login_required
def CaseManagerTable(request):
      with conn.cursor() as cursor:
        cursor.execute(
            '''SELECT *
             FROM Case_Model 
             WHERE User_ID = %s OR CaseManager_ID = %s
             ORDER BY Created_at DESC
             ''', [request.user.id, request.user.id] 
            )
        columns = [col[0] for col in cursor.description]
        cases = [dict(zip(columns, row))for row in cursor.fetchall()]
        return render(request,'scrCaseManagerTable.html', {'cases': cases})
@login_required
def CaseManagerTableAll(request):
     with conn.cursor() as cursor:
          cursor.execute(
               '''Select * 
               FROM Case_Model
               ORDER BY Created_at DESC
               '''
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
            staffs = User.objects.filter(is_staff=True, is_active=True)
            if not case['casemanager_id']:
                 assigned =  "Velg ansatt"
            else: 
                assigned = getCaseManagerName(case['casemanager_id'])
        else:   
            case = None
            
    return render(request, 'scrCaseManagerView.html', {'case': case, 'staffs':staffs, 'assigned': assigned })

@login_required 
def CaseManagerUpdateCase(request, case_id):
    if request.method == 'POST':
        newstat = request.POST['status']    
        appointment_date = request.POST['Appointment_date']
        assigned_to = request.POST['assigned_to']
        if not appointment_date :
            appointment_date = None
        if not newstat:
            newstat = None

        with conn.cursor() as cursor:
            cursor.execute(
                'Select * from UpdateCase(%s,%s,%s,%s)'
                , [case_id,newstat,appointment_date, assigned_to ]
            )
            result = cursor.fetchone()
            if result[1]:
                    messages.success(request, result[2])
                    return redirect('scrCaseManagerView',case_id=case_id)
            else:
                    messages.error(request, result[2])
        return redirect('scrCaseManagerView', case_id=case_id)
        
    
