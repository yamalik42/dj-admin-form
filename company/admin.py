from django.contrib import admin
from .models import Employee, Manager

# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'age',
        'department',
        'created_date',
        'modified_date',
    )
    list_filter = (
        'age',
    )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'age',
        'salary',
        'designation',
        'created_date',
        'modified_date',
        'reporting_manager',
    )
    list_filter = (
        'age',
        'salary',
    )
    search_fields = ['name']
    fieldsets = (
            ('Personal', {
                'fields': ('name', 'age'),
            }),
            ('Work', {
                'fields': ('designation', 'salary'),
            }),
            ('Supervisor', {
                'fields': ('reporting_manager',),
            }),
        )

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Manager, ManagerAdmin)
