from django.db import models
from django.conf import settings




# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# Teacher Model
class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    # অন্যান্য প্রয়োজনীয় ফিল্ড
    def __str__(self):
        return f"{self.user.username} ({self.employee_id})"

# Student Model
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    # অন্যান্য প্রয়োজনীয় ফিল্ড
    def __str__(self):
        return f"{self.user.username} ({self.roll_number})"

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return self.title

# Result Model
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.roll} - {self.course.code} ({self.marks})"
