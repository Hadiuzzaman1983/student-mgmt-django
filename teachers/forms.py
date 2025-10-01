from django import forms
from .models import Teacher

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'email', 'phone', 'join_date']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),
        }
