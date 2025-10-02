from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ClassRoutine, Grade, Assignment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Grade, Teacher



class TeacherDashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "teachers/dashboard_home.html"



# ---------- Class Routine ----------
# teachers/views.py
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ClassRoutine


class TeacherClassRoutineListView(LoginRequiredMixin, ListView):
    model = ClassRoutine
    template_name = "teachers/class_routine_list.html"
    context_object_name = "routines"

    def get_queryset(self):
        # শুধুমাত্র লগইন করা Teacher এর রুটিন দেখাবে
        try:
            teacher = Teacher.objects.get(user=self.request.user)
            return ClassRoutine.objects.filter(teacher=teacher).order_by('day', 'time')
        except Teacher.DoesNotExist:
            return ClassRoutine.objects.none()

class ClassRoutineListView(ListView):
    model = ClassRoutine
    template_name = "teachers/class_routine_list.html"
    context_object_name = "routines"

# Routine CreateView
class ClassRoutineCreateView(CreateView):
    model = ClassRoutine
    fields = ['subject', 'subject_code', 'day', 'time']   # ✅ subject_code যুক্ত
    template_name = "teachers/class_routine_form.html"
    success_url = reverse_lazy('class_routine_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)


# ---------- Grade ----------

# teachers/views.py
class TeacherGradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "teachers/grade_list.html"
    context_object_name = "grades"

    def get_queryset(self):
        try:
            teacher = Teacher.objects.get(user=self.request.user)
            return Grade.objects.filter(teacher=teacher).order_by('student__user__username', 'subject')
        except Teacher.DoesNotExist:
            return Grade.objects.none()

class GradeListView(ListView):
    model = Grade
    template_name = "teachers/grade_list.html"
    context_object_name = "grades"

# Grade CreateView
class GradeCreateView(CreateView):
    model = Grade
    fields = ['student_name', 'subject', 'subject_code', 'marks', 'grade']  # ✅ subject_code যুক্ত
    template_name = "teachers/grade_form.html"
    success_url = reverse_lazy('grade_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)


# ---------- Assignment ----------
class AssignmentListView(ListView):
    model = Assignment
    template_name = "teachers/assignment_list.html"
    context_object_name = "assignments"

class AssignmentCreateView(CreateView):
    model = Assignment
    fields = ['title', 'description', 'file']
    template_name = "teachers/assignment_form.html"
    success_url = reverse_lazy('assignment_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
