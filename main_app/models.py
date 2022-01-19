from django.contrib.auth.models import AbstractUser
from django.db import models 
from datetime import datetime    
from django.urls import reverse

# General User login
class User(AbstractUser):
    TYPE_CHOICES = (
        ('M', 'Member'),
        ('S', 'Staff'),
    )
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    user_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='M')

    def __str__(self):
        # return f"{self.get_user_type_display()}"
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('books_detail', kwargs={'books_id': self.id})
    

# User split into either Member or Staff --------------------------------
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # books_rented = models.ManyToManyField(Books)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_absolute_url(self):
        return reverse('members_detail', kwargs={'members_id': self.id})

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # shifts_per_week = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

# ------------------------------------------------------------------------

# Many club has many members - Club model holds key of Members
class Club(models.Model):
    ROOMS = (
        ('-', 'No meeting place assigned to this club'),
        ('a', '1st Floor Auditorium'),
        ('b', '1st Floor Large Study Room'),
        ('c', '2nd Floor Meeting Room'),
    )

    name = models.CharField(max_length=50)
    meet_date = models.DateField(default='YYYY-MM-DD')

    # staff should be able to add more rooms depending on library size
    location = models.CharField(max_length=1, choices=ROOMS, default='-')
    desc = models.TextField(max_length=100, blank=False)
    members = models.ManyToManyField(Member)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def show_club_president(self):
        pass

    


 