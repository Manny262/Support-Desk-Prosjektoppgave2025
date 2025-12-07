from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection as conn 

@login_required 
def UserMain(request):
    return render(request, 'scrUserMain.html')
@login_required 
def UserTable(request):
    with conn.cursor() as cursor:
        cursor.execute(
            '''SELECT Case_ID, Title, Description, 
                      Category, Urgency, Status, 
                      Created_at
             FROM Case_Model 
             WHERE User_ID = %s
             ORDER BY Created_at DESC
             ''', [request.user.id] 
            )
        columns = [col[0] for col in cursor.description]
        cases = [dict(zip(columns, row))for row in cursor.fetchall()]

    return render(request, 'scrUserTable.html', {'cases': cases
    })

@login_required 
def UserView(request):
    return render(request, 'scrUserView.html')

