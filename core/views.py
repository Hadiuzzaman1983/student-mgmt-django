from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Teacher, Department, Course
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    menu = [
        {"label": "Dashboard", "url": "/dashboard/admin/"},
        {"label": "Manage Teachers", "url": "/teachers/"},
        {"label": "Manage Students", "url": "/students/"},
        {"label": "Courses", "url": "/courses/"},
        {"label": "Results", "url": "/results/"},
    ]
    return render(request, "core/admin_dashboard.html", {"menu": menu})

@login_required
def teacher_dashboard(request):
    menu = [
        {"label": "Dashboard", "url": "/dashboard/teacher/"},
        {"label": "My Classes", "url": "/teacher/classes/"},
        {"label": "Enter Marks", "url": "/teacher/marks/"},
        {"label": "Notices", "url": "/notices/"},
    ]
    return render(request, "core/teacher_dashboard.html", {"menu": menu})

@login_required
def student_dashboard(request):
    menu = [
        {"label": "Dashboard", "url": "/dashboard/student/"},
        {"label": "My Profile", "url": "/student/profile/"},
        {"label": "My Courses", "url": "/student/courses/"},
        {"label": "Results", "url": "/student/results/"},
        {"label": "Notices", "url": "/notices/"},
    ]
    return render(request, "core/student_dashboard.html", {"menu": menu})

# Student List View
class StudentListView(ListView):
    model = Student
    template_name = "core/student_list.html"
    context_object_name = "students"

# Student Detail View
class StudentDetailView(DetailView):
    model = Student
    template_name = "core/student_detail.html"
    context_object_name = "student"

# Student Create View
class StudentCreateView(CreateView):
    model = Student
    fields = ["user", "roll", "department", "semester"]
    template_name = "core/student_form.html"
    success_url = reverse_lazy("student_list")

# Student Update View
class StudentUpdateView(UpdateView):
    model = Student
    fields = ["user", "roll", "department", "semester"]
    template_name = "core/student_form.html"
    success_url = reverse_lazy("student_list")

# Student Delete View
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "core/student_confirm_delete.html"
    success_url = reverse_lazy("student_list")
