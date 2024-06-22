from django.contrib import admin
from core.models import DayType, Employee, Timecard, Department

# Register your models here.


class TimecardAdmin(admin.ModelAdmin):
    list_display = ['date', 'employer', 'day_type']
    fields = ['id', 'date', 'employer', 'day_type']
    readonly_fields = ['id']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['id', 'name']
    readonly_fields = ['id']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'patronymic', 'email', 'date_birth', 'department']
    fields = ['id', 'name', 'surname', 'patronymic', 'email', 'date_birth', 'department']
    readonly_fields = ['id']


class DayTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'mark']
    fields = ['id', 'name', 'mark']
    readonly_fields = ['id']


admin.site.register(DayType, DayTypeAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Timecard, TimecardAdmin)
admin.site.register(Department, DepartmentAdmin)
