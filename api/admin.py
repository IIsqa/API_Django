from django.contrib import admin

# Register your models here.
from .models import (
    Department,
    Position,
    Employee,
)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'department', 'created_at', 'updated_at')
    search_fields = ('name', 'department__name')
    list_filter = ('department', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

from django.utils.html import format_html

from django.contrib import admin
from django.utils.html import format_html
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'id',
        'name',
        'surname',
        'email',
        'department',
        'position',
        'status',
        'created_at',
        'updated_at',
        'display_profile_picture'
    )

    # Fields to search within the admin interface
    search_fields = (
        'name',
        'surname',
        'email',
        'department__name',
        'position__name'
    )

    # Fields to filter the admin list view
    list_filter = (
        'department',
        'position',
        'status',
        'created_at',
        'updated_at'
    )

    # Read-only fields for the admin interface
    readonly_fields = ('created_at', 'updated_at')

    def display_profile_picture(self, obj):
        """Display the profile picture from the related documents."""
        # Get the first document with a profile picture for the employee
        document = obj.documents.filter(profile_picture__isnull=False).first()
        if document and document.profile_picture:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px;"/>',
                document.profile_picture.url
            )
        return "No Image"

    display_profile_picture.short_description = 'Profile Picture'


    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)