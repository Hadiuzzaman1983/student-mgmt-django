from django.urls import path
from .import views
from .views import *

urlpatterns = [
    # Dashboard
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/teacher/", views.teacher_dashboard, name="teacher_dashboard"),
    path("dashboard/student/", views.student_dashboard, name="student_dashboard"),

    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/add/", StudentCreateView.as_view(), name="student_add"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="student_edit"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
]
