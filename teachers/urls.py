from django.urls import path
from .views import *


urlpatterns = [
    path('', TeacherDashboardHomeView.as_view(), name='teacher_dashboard'),
    #profile
    path('profile/', TeacherProfileView.as_view(), name='teacher_profile'),
    path('profile/edit/', TeacherProfileUpdateView.as_view(), name='teacher_profile_edit'),

    # Routine
    path('class-routine/', TeacherClassRoutineListView.as_view(), name='teacher_class_routine_list'),
    path('grades/', TeacherGradeListView.as_view(), name='teacher_grade_list'),
    path('routines/', ClassRoutineListView.as_view(), name='class_routine_list'),
    path('routines/add/', ClassRoutineCreateView.as_view(), name='class_routine_add'),
    path('routines/create/', ClassRoutineCreateView.as_view(), name='class_routine_create'),

    # Grade
    path('grades/', GradeListView.as_view(), name='grade_list'),
    path('grades/add/', GradeCreateView.as_view(), name='grade_add'),

    path('assignments/', TeacherAssignmentListView.as_view(), name='teacher_assignment_list'),
    path('assignments/create/', TeacherAssignmentCreateView.as_view(), name='teacher_assignment_create'),
    path('assignments/<int:pk>/edit/', TeacherAssignmentUpdateView.as_view(), name='teacher_assignment_update'),
    path('assignments/<int:pk>/delete/', TeacherAssignmentDeleteView.as_view(), name='teacher_assignment_delete'),

    path('notices/', TeacherNoticeListView.as_view(), name='teacher_notice_list'),
    path('notices/create/', TeacherNoticeCreateView.as_view(), name='teacher_notice_create'),
    path('notices/<int:pk>/edit/', TeacherNoticeUpdateView.as_view(), name='teacher_notice_update'),
    path('notices/<int:pk>/delete/', TeacherNoticeDeleteView.as_view(), name='teacher_notice_delete'),
]
