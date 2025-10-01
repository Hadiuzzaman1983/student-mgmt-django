from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Teacher
from .forms import TeacherRegistrationForm

class TeacherRegisterView(CreateView):
    model = Teacher
    form_class = TeacherRegistrationForm
    template_name = 'teachers/teacher_register.html'
    success_url = reverse_lazy('teacher_success')
