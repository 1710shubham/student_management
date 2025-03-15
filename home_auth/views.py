from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password

# Create your views here.


def  signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # cpassword = request.POST['cpassword']
        username = request.POST['username']  # Add the username field here

        # role = request.POST['role']



        #create the user
        user = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            # cpassword = cpassword,
            username=username,
            # role=role
        )
        
        # if role == 'student':
        #     user.is_student = True
        
        # elif role == 'teacher':
        #     user.is_teacher = True

        # elif role == 'admin':
        #     user.is_admin = True
            
        user.save()
        login(request,user)
        messages.success(request,'signup Successfully!')
        return render(request,"auth/login.html")

    return render(request,"auth/register.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,email = email ,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Suceesfully!')

            if user.is_admin:
                return redirect("admin _dashboard")
            
            elif user.is_teacher:
                return redirect("teacher _dashboard")

            elif user.is_student:
                return redirect('index')

            else:
                messages.error(request,'Invalid user role')
                return redirect('index')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request, "students/student-dashboard.html")

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = CustomUser.objects.filter(email=email).first()

        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(user=user,email=email,token=token)
            reset_request.send_reset_email()
            messages.success(request,'Reset link sent to your email.')

        else:
            messages.error(request,'Email not found')
    return render(request,'auth/forget-password.html')


def reset_password_view(request,token):
    reset_request = PasswordResetRequest.objects.filter(token=token)

    if not reset_request or not reset_request.is_valid():
        messages.error(request,'Invalid')
        return redirect('index')

    if request.method == 'POST':
        new_password = request.POST['new_password']
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request,'Password Reset Successfully')
        return redirect('login')
        
    return render(request,'reset_password.html',{'token: token'})

def logout_view(request):
    logout(request)
    messages.success(request,'You Have Been logged out')
    return redirect('index')