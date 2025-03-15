from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Index(request):
    return render(request,"auth/login.html")


def dashboard(request):
    return render(request,"student/student-dashboard.html")