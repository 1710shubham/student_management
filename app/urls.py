from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Index,name="index"),
    path('dashboard/',views.dashboard,name="dashboard"),


]