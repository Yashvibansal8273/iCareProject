from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('username', 'email', 'mobile_number', 'is_staff', 'is_active', 'date_joined')

    # Define the fields to be used for searching
    search_fields = ('username', 'email', 'mobile_number')

    # Define the fields that are editable in the admin form
    list_filter = ('is_staff', 'is_active', 'date_joined')

    # Add the fields to be displayed in the detail view of the user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'mobile_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add the fields to be displayed in the list view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'mobile_number', 'is_active', 'is_staff')}
        ),
    )

# Register the custom user model with the admin interface
admin.site.register(CustomUser, CustomUserAdmin)
