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
    phone = models.CharField(max_length=20, blank=True)
    # অন্যান্য প্রয়োজনীয় ফিল্ড
    def __str__(self):
        return f"{self.user.username} ({self.employee_id})"

# Student Model
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    admission_date = models.DateField(auto_now_add=True)
    # অন্যান্য প্রয়োজনীয় ফিল্ড
    def __str__(self):
        return f"{self.user.username} ({self.roll_number})"

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

# Attendance Model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(("Present", "Present"), ("Absent", "Absent")))

    def __str__(self):
        return f"{self.student.name} - {self.course.name} - {self.date}"

# Result Model
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.name} - {self.grade}"

# Notice Board
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Fee Collection
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(("Paid", "Paid"), ("Unpaid", "Unpaid")))

    def __str__(self):
        return f"{self.student.name} - {self.amount} ({self.status})"