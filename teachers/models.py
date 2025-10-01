from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    join_date = models.DateField()

    def __str__(self):
        return self.name
