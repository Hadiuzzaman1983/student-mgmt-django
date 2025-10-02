from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView
from accounts.mixins import AdminRequiredMixin, TeacherRequiredMixin, StudentRequiredMixin
from accounts.decorators import admin_required

@admin_required
def admin_home(request):
    return render(request, 'dashboard/admin_dashboard.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

# Dashboard with Role Based Access
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role == 'admin':
            template = 'dashboard/admin_dashboard.html'
        elif request.user.role == 'teacher':
            template = 'dashboard/teacher_dashboard.html'
        elif request.user.role == 'student':
            template = 'dashboard/student_dashboard.html'
        else:
            template = 'dashboard/default_dashboard.html'
        return render(request, template)

class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = "dashboard/admin_dashboard.html"

class TeacherDashboardView(TeacherRequiredMixin, TemplateView):
    template_name = "dashboard/teacher_dashboard.html"

class StudentDashboardView(StudentRequiredMixin, TemplateView):
    template_name = "dashboard/student_dashboard.html"