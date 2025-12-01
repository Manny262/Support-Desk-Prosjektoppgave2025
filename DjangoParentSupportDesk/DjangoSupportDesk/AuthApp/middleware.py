from django.shortcuts import redirect
from django.contrib import messages

class BlockStaff:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if request.user.is_authenticated and request.user.is_staff and not request.user.is_superuser:
                messages.error(request, 'Du har ikke tilgang til admin-panelet')
                return redirect('scrLogin')
        
        response = self.get_response(request)
        return response

class Staffredirect:
        def __init__(self, get_response):
            self.get_response = get_response
        
        def __call__(self, request):          
            if request.path.startswith('/Case') or request.path.startswith('/scrCase') and request.user.is_authenticated:
                if request.user.is_staff:
                    response = self.get_response(request)
                    return response
                else:
                    return redirect('scrUserMain')
            
            response = self.get_response(request)
            return response



        