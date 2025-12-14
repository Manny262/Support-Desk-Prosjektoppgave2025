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
def UserMain(request):
    return render(request, 'scrUserMain.html')
@login_required 
def UserTable(request):
    with conn.cursor() as cursor:
        cursor.execute(
            '''SELECT Case_ID, Title, Status, Appointment_date, Category,
                      Created_at
             FROM Case_Model 
             WHERE User_ID = %s
             ORDER BY Created_at DESC
             ''', [request.user.id] 
            )
        columns = [col[0] for col in cursor.description]
        cases = [dict(zip(columns, row))for row in cursor.fetchall()]
        print(cases)
    return render(request, 'scrUserTable.html', {'cases': cases
    })

@login_required 
def UserView(request, case_id):
     with conn.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM GetCase(%s)',
            [case_id]
        )
        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            case = dict(zip(columns, row))
            if case['have_comments'] == True:
                comments = getComments(case_id)            
            else: 
                comments = None 
                print("none")      
            if not case['casemanager_id']:
                 assigned =  "Velg ansatt"
            else: 
                assigned = getName (case['casemanager_id'])                  
     return render(request, 'scrUserView.html', {'case': case, 'comments': comments})

def UserNewComment(request, case_id, bool_param):
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

    return redirect('scrUserView', case_id=case_id)