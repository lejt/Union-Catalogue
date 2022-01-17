from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime  

# Create your models here.
class User(AbstractUser):
    # is_lib_member = models.BooleanField('is member', default=False)
    # is_lib_staff = models.BooleanField('is staff', default=False)
    TYPE_CHOICES = (
        ('M', 'Member'),
        ('S', 'Staff'),
    )
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='M')

class Books(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

class Member(models.Model):
    user_memb = models.OneToOneField(User, on_delete=models.CASCADE)
    # books_rented = models.ManyToManyField(Books)

class Staff(models.Model):
    user_staff = models.OneToOneField(User, on_delete=models.CASCADE)
    # shifts_per_week = models.IntegerField(default=5)





 