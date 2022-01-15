from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_member = models.BooleanField('member status', default=False)
    is_staff = models.BooleanField('staff status', default=False)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)