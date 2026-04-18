from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('hospital', 'Hospital'),
        ('parent', 'Parent'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return f"{self.username} ({self.role})"

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    def __str__(self):
        return self.user.username

class Hospital(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,  blank=True )
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    logo = models.ImageField(upload_to='hospital_logos/', blank=True, null=True)
    def __str__(self):
        return self.name