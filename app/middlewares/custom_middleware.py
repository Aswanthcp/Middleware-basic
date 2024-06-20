from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from app import views
from app.models import CustomUser as User


class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/login/':
            print('login Requst')
            
        elif request.path == '/logout/':
            # Handle logout logic
            print("Logout Request")
            # You can perform any additional actions related to logout here
        elif request.path == '/admin/' :
            print("Admin")
            
        elif request.user.is_authenticated:
            role = request.user.role
            print(role)
            if role == 'teacher' and not request.path.startswith('/teacher_home'):
                return redirect('teacher_home')
            elif role == 'student' and not request.path.startswith('/student_home'):
                return redirect('student_home')
            elif role == 'principal' and not request.path.startswith('/principal_home'):
                return redirect('principal_home')
            