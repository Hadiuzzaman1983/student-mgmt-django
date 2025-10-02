from django.db import models
from django.conf import settings
from .models Teacher

# Teacher Model ধরে নেওয়া হচ্ছে আগে থেকেই আছে

# ক্লাস রুটিন
class ClassRoutine(models.Model):
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)   # ✅ নতুন ফিল্ড
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=[
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ])
    time = models.TimeField()

    def __str__(self):
        return f"{self.subject} ({self.subject_code}) - {self.day} ({self.time})"


# মার্কস / গ্রেড এন্ট্রি
class Grade(models.Model):
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)   # ✅ নতুন ফিল্ড
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student_name} - {self.subject} ({self.subject_code}) : {self.grade}"


# অ্যাসাইনমেন্ট আপলোড
class Assignment(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='assignments/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

