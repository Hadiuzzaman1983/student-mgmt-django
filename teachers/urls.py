from django.urls import path
from .views import (
    ClassRoutineListView, ClassRoutineCreateView,
    GradeListView, GradeCreateView,
    AssignmentListView, AssignmentCreateView, TeacherDashboardHomeView,
    TeacherClassRoutineListView
)

urlpatterns = [
    path('', TeacherDashboardHomeView.as_view(), name='teacher_dashboard'),
    # Routine
    path('class-routine/', TeacherClassRoutineListView.as_view(), name='teacher_class_routine_list'),
    path('grades/', TeacherGradeListView.as_view(), name='teacher_grade_list'),
    path('routines/', ClassRoutineListView.as_view(), name='class_routine_list'),
    path('routines/add/', ClassRoutineCreateView.as_view(), name='class_routine_add'),
    path('routines/create/', ClassRoutineCreateView.as_view(), name='class_routine_create'),

    # Grade
    path('grades/', GradeListView.as_view(), name='grade_list'),
    path('grades/add/', GradeCreateView.as_view(), name='grade_add'),

    # Assignment
    path('assignments/', AssignmentListView.as_view(), name='assignment_list'),
    path('assignments/add/', AssignmentCreateView.as_view(), name='assignment_add'),
]
