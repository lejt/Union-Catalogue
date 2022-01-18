
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

from django import forms

class LoginForm(UserCreationForm):
    pass

# https://www.youtube.com/watch?v=TBGRYkzXiTg&ab_channel=Codemy.com
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_type']
