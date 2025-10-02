from django.db import models
from django.conf import settings

# Student Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roll = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.roll})"


# Course
class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    credit = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.code} - {self.name}"


# Result
class Result(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.roll} - {self.course.code} ({self.grade})"


# Class Routine
class ClassRoutine(models.Model):
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    day = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.department} Sem-{self.semester} {self.day} {self.subject}"


# Notice
class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
