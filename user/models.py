from django.db import models
# Create your models here.


class Registeration(models.Model):
    ROLES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
      
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLES)
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    mobile= models.CharField(max_length=10)
    password = models.CharField(max_length=255)