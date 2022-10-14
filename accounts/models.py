from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.urls import reverse

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)