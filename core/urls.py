from django.urls import path
from .import views
from .views import *

urlpatterns = [
    # Dashboard
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/teacher/", views.teacher_dashboard, name="teacher_dashboard"),
    path("dashboard/student/", views.student_dashboard, name="student_dashboard"),

# Departments
    path("departments/", views.DepartmentListView.as_view(), name="department_list"),
    path("departments/<int:pk>", views.DepartmentListView.as_view(), name="department_detail"),
    path("departments/add/", views.DepartmentCreateView.as_view(), name="department_add"),
    path("departments/create/", DepartmentCreateView.as_view(), name="department_create"),
    path("departments/<int:pk>/update/", DepartmentUpdateView.as_view(), name="department_update"),
    path("departments/<int:pk>/edit/", views.DepartmentUpdateView.as_view(), name="department_edit"),
    path("departments/<int:pk>/delete/", views.DepartmentDeleteView.as_view(), name="department_delete"),

    # Teachers
    path("teachers/", views.TeacherListView.as_view(), name="teacher_list"),
    path("teachers/<int:pk>", views.TeacherDetailView.as_view(), name="teacher_detail"),
    path("teachers/add/", views.TeacherCreateView.as_view(), name="teacher_add"),
    path("teachers/<int:pk>/update/", views.TeacherUpdateView.as_view(), name="teacher_update"),
    path("teachers/<int:pk>/edit/", views.TeacherUpdateView.as_view(), name="teacher_edit"),
    path("teachers/<int:pk>/delete/", views.TeacherDeleteView.as_view(), name="teacher_delete"),

    # Students
    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/add/", StudentCreateView.as_view(), name="student_create"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("students/add/", StudentCreateView.as_view(), name="student_add"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="student_edit"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
]
