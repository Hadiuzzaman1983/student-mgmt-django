from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'department')
    search_fields = ('user__username', 'roll_number', 'department')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department')
    search_fields = ('user__username', 'employee_id', 'department')

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Result)
admin.site.register(Notice)
admin.site.register(Fee)