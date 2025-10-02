from django.contrib import admin
from .models import ClassRoutine, Grade, Assignment


@admin.register(ClassRoutine)
class ClassRoutineAdmin(admin.ModelAdmin):
    list_display = ('subject', 'subject_code', 'teacher', 'day', 'time')
    list_filter = ('day', 'teacher', 'subject_code')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'subject', 'subject_code', 'teacher', 'marks', 'grade')
    list_filter = ('subject', 'subject_code', 'grade')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'created_at')
    search_fields = ('title',)










