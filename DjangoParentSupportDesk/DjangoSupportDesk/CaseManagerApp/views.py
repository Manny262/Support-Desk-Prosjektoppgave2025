from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection as conn
from django.contrib.auth.models import User

def getName (id):
    if id:
        return User.objects.get(id=id).username

def getComments(case_id):
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM GetComments(%s)',
            [case_id]
        )
        commentsColumns = [col[0] for col in cursor.description]
        commentsRows = cursor.fetchall()    

        if commentsRows:
            comments = [dict(zip(commentsColumns, row)) for row in commentsRows]
        else:
            comments = []
        
        return comments


@login_required 
def CaseManagerMain(request):
    return render(request,'scrCaseManagerMain.html', {'Name': getName (request.user.id)})
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
            
            if case['have_comments'] == True:
                comments = getComments(case_id)
            else: 
                comments = None 
                print("none")

            if not case['casemanager_id']:
                 assigned =  "Velg ansatt"
            else: 
                assigned = getName (case['casemanager_id'])
        else:   
            case = None
            
    return render(request, 'scrCaseManagerView.html', {'case': case, 'staffs':staffs, 'assigned': assigned, 'comments' : comments})

@login_required 
def CaseManagerUpdateCase(request, case_id):
    if request.method == 'POST':
        newstat = request.POST['status']    
        appointment_date = request.POST['Appointment_date']
        assigned_to = int(request.POST['assigned_to'])
        if not appointment_date :
            appointment_date = None
        if not newstat:
            newstat = None
        if not assigned_to or assigned_to == 0:
             assigned_to = None 
        with conn.cursor() as cursor:
            cursor.execute(
                'Select * from UpdateCase(%s,%s,%s,%s)'
                , [case_id,newstat,appointment_date, assigned_to ]
            )
            result = cursor.fetchone()
            if result[1]:
                    messages.success(request, result[2])
                    print(result)
            else:
                    messages.error(request, result[2])
    
    return redirect('scrCaseManagerView', case_id=case_id)

def CaseManagerNewComment(request, case_id, bool_param):
    if request.method == 'POST':

        newComment = request.POST['inpNewComment']
        if not newComment:
            messages.error(request, "Ingen kommentarer")
        else:
            with conn.cursor() as cursor:
                cursor.execute(
                    'Select * from NewComment(%s,%s,%s)',
                    [request.user.id, case_id, newComment]
                )
                result = cursor.fetchone()
                if result[1]:
                    messages.success(request, result[2])
                    if bool_param.lower() == 'false':
                        cursor.execute(
                            '''UPDATE Case_Model
                                SET Have_Comments = true
                                WHERE case_id = %s
                            ''', [case_id]
                        )
                        conn.commit()
                else:
                    messages.error(request, result[2])

    return redirect('scrCaseManagerView', case_id=case_id)

            