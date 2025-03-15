from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("signup/",views.signup_view,name="signup"),
    path("login/",views.login_view,name="login"),
    path("forget-password/",views.forgot_password_view,name="forget_password"),
    path("reset-password/<str:token>/",views.reset_password_view,name="reset_password"),
    path("logout/",views.login_view,name="logout"),
    
]