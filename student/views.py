from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StudentProfile, Result, Course, ClassRoutine, Notice
from django.urls import reverse_lazy
from django.contrib import messages


class StudentDashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "students/dashboard_home.html"

# Student Profile View

class StudentProfileView(DetailView):
    model = StudentProfile
    template_name = "students/profile.html"
    context_object_name = "profile"

    def get_object(self):
        try:
            return StudentProfile.objects.get(user=self.request.user)
        except StudentProfile.DoesNotExist:
            return redirect("student_profile_create")  # আপনার profile create view এর url name


class StudentProfileCreateView(LoginRequiredMixin, CreateView):
    model = StudentProfile
    template_name = "students/profile_form.html"
    fields = ["full_name", "roll", "semester", "department", "course", "phone"]
    success_url = reverse_lazy("student_profile")

    def form_valid(self, form):
        form.instance.user = self.request.user  # profile এই ইউজারের সাথে link হবে
        return super().form_valid(form)


# Result List View
class ResultListView(LoginRequiredMixin, ListView):
    model = Result
    template_name = "students/result_list.html"

    def get_queryset(self):
        return Result.objects.filter(student__user=self.request.user)


# Course List View
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "students/course_list.html"


# Class Routine List View
class RoutineListView(LoginRequiredMixin, ListView):
    model = ClassRoutine
    template_name = "students/routine_list.html"

    def get_queryset(self):
        try:
            profile = StudentProfile.objects.get(user=self.request.user)
        except StudentProfile.DoesNotExist:
            messages.warning(self.request, "Please create your profile first.")
            return redirect("student_profile_create")

        return Routine.objects.filter(semester=profile.semester)


# Notice List View
class NoticeListView(LoginRequiredMixin, ListView):
    model = Notice
    template_name = "students/notice_list.html"
    queryset = Notice.objects.all().order_by('-created_at')


