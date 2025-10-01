from django.urls import path
from .views import TeacherRegisterView
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', TeacherRegisterView.as_view(), name='teacher_register'),
    path('register/success/', TemplateView.as_view(template_name='teachers/register_success.html'), name='teacher_success'),
]
