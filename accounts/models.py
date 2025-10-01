from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # প্রয়োজন হলে extra fields যোগ করতে পারেন
    # উদাহরণ:
    # phone = models.CharField(max_length=15, blank=True, null=True)
    pass
