from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ClassRoutine, Grade, Assignment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Grade,Teacher,Assignment,Notice


class TeacherDashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "teachers/dashboard_home.html"


# View to see own profile
class TeacherProfileView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = "teachers/teacher_profile.html"
    context_object_name = "teacher"

    def get_object(self, queryset=None):
        return Teacher.objects.get(user=self.request.user)

# View to edit profile
class TeacherProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    fields = ['full_name', 'department', 'subject', 'email', 'phone']
    template_name = "teachers/teacher_profile_form.html"
    success_url = reverse_lazy('teacher_profile')

    def get_object(self, queryset=None):
        return Teacher.objects.get(user=self.request.user)


# ---------- Class Routine ----------
# teachers/views.py

class TeacherClassRoutineListView(LoginRequiredMixin, ListView):
    model = ClassRoutine
    template_name = "teachers/class_routine_list.html"
    context_object_name = "routines"

    def get_queryset(self):
        return ClassRoutine.objects.filter(teacher=self.request.user)

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
        # যদি Grade model-এ teacher = ForeignKey(User)
        return Grade.objects.filter(teacher=self.request.user)

class GradeListView(ListView):
    model = Grade
    template_name = "teachers/grade_list.html"
    context_object_name = "grades"

# Grade CreateView
class GradeCreateView(CreateView):
    model = Grade
    fields = ["employee_id", "full_name", "department", "subject", "email", "phone", "user"] # ✅ subject_code যুক্ত
    template_name = "teachers/grade_form.html"
    success_url = reverse_lazy('grade_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)



# List View
class TeacherAssignmentListView(ListView):
    model = Assignment
    template_name = "teachers/teacher_assignment_list.html"
    context_object_name = "assignments"

    def get_queryset(self):
        return Assignment.objects.filter(teacher=self.request.user)

# Create View
class TeacherAssignmentCreateView(CreateView):
    model = Assignment
    fields = ['title', 'description', 'file']
    template_name = "teachers/teacher_assignment_form.html"
    success_url = reverse_lazy('teacher_assignment_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

# Update View
class TeacherAssignmentUpdateView(UpdateView):
    model = Assignment
    fields = ['title', 'description', 'file']
    template_name = "teachers/teacher_assignment_form.html"
    success_url = reverse_lazy('teacher_assignment_list')

# Delete View
class TeacherAssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = "teachers/teacher_assignment_confirm_delete.html"
    success_url = reverse_lazy('teacher_assignment_list')



class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ["employee_id", "full_name", "department", "subject", "email", "phone", "user"]
    template_name = "teachers/teacher_form.html"
    success_url = reverse_lazy("teacher_list")


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = "teachers/teacher_confirm_delete.html"
    success_url = reverse_lazy("teacher_list")



# List View
class TeacherNoticeListView(ListView):
    model = Notice
    template_name = "teachers/teacher_notice_list.html"
    context_object_name = "notices"

    def get_queryset(self):
        return Notice.objects.filter(teacher=self.request.user).order_by('-created_at')

# Create View
class TeacherNoticeCreateView(CreateView):
    model = Notice
    fields = ['title', 'content']
    template_name = "teachers/teacher_notice_form.html"
    success_url = reverse_lazy('teacher_notice_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

# Update View
class TeacherNoticeUpdateView(UpdateView):
    model = Notice
    fields = ['title', 'content']
    template_name = "teachers/teacher_notice_form.html"
    success_url = reverse_lazy('teacher_notice_list')

# Delete View
class TeacherNoticeDeleteView(DeleteView):
    model = Notice
    template_name = "teachers/teacher_notice_confirm_delete.html"
    success_url = reverse_lazy('teacher_notice_list')