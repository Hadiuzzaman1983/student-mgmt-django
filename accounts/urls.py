from django.urls import path
from .views import *

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('teacher/', TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('student/', StudentDashboardView.as_view(), name='student_dashboard'),
]
