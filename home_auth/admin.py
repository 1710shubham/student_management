from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None,{'fields':('user_name','password')}),#Login
        ('Personal Info',{'fields':('first_name','last_name','email')}),
        ('Roles',{'fields':('is_student','is_teacher','is_admin')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 
                       'is_authorized', 'is_student', 'is_teacher', 'is_admin')}
        ),
    )

    list_display = ('username', 'email', 'is_authorized', 'is_student', 'is_teacher', 'is_admin', 'is_staff')
    list_filter = ('is_authorized', 'is_student', 'is_teacher', 'is_admin', 'is_staff')


# admin.site.register(CustomUser,CustomUserAdmin)