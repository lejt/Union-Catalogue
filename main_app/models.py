from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# General User login
class User(AbstractUser):
    # is_lib_member = models.BooleanField('is member', default=False)
    # is_lib_staff = models.BooleanField('is staff', default=False)
    TYPE_CHOICES = (
        ('M', 'Member'),
        ('S', 'Staff'),
    )
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='M')

    def __str__(self):
        return f"{self.get_user_type_display()}"

class Books(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)


# User split into either Member or Staff --------------------------------
class Member(models.Model):
    user_memb = models.OneToOneField(User, on_delete=models.CASCADE)
    # books_rented = models.ManyToManyField(Books)

class Staff(models.Model):
    user_staff = models.OneToOneField(User, on_delete=models.CASCADE)
    # shifts_per_week = models.IntegerField(default=5)
# ------------------------------------------------------------------------

# A club has many members
class Club(models.Model):
    ROOMS = (
        ('a', '1st Floor Auditorium'),
        ('b', '1st Floor Large Study Room'),
        ('c', '2nd Floor Meeting Room'),
    )

    name = models.CharField(max_length=50)
    meet_date = models.DateField()

    # staff should be able to add more rooms depending on library size
    # location = models.CharField(max_length=1, choices=ROOMS)
    desc = models.TextField(max_length=100)
    # popul = models.ManyToManyField(Member)
    


 