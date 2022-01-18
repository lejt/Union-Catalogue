from django.contrib.auth.models import AbstractUser
from django.db import models 
import datetime
from django.urls import reverse

# General User login
class User(AbstractUser):
    TYPE_CHOICES = (
        ('M', 'Member'),
        ('S', 'Staff'),
    )
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='M')

    def __str__(self):
        return f"{self.get_user_type_display()}"

class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('books_detail', kwargs={'books_id': self.id})
    

# User split into either Member or Staff --------------------------------
class Member(models.Model):
    user_memb = models.OneToOneField(User, on_delete=models.CASCADE)
    # books_rented = models.ManyToManyField(Books)

    def __str__(self):
        return self.user_memb.first_name

class Staff(models.Model):
    user_staff = models.OneToOneField(User, on_delete=models.CASCADE)
    # shifts_per_week = models.IntegerField(default=5)

    def __str__(self):
        return self.user_staff.first_name
# ------------------------------------------------------------------------

# Many club has many members - Club model holds key of Members
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
    members = models.ManyToManyField(Member)


    


 