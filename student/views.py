from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StudentProfile, Result, Course, ClassRoutine, Notice


class StudentDashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "students/dashboard_home.html"

# Student Profile View
class StudentProfileView(LoginRequiredMixin, DetailView):
    model = StudentProfile
    template_name = "students/profile.html"

    def get_object(self):
        return StudentProfile.objects.get(user=self.request.user)


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
        student = StudentProfile.objects.get(user=self.request.user)
        return ClassRoutine.objects.filter(
            department=student.department, semester=student.semester
        )


# Notice List View
class NoticeListView(LoginRequiredMixin, ListView):
    model = Notice
    template_name = "students/notice_list.html"
    queryset = Notice.objects.all().order_by('-created_at')
