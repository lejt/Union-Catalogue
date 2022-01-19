
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Club
from django import forms

class LoginForm(UserCreationForm):
    pass

# https://www.youtube.com/watch?v=TBGRYkzXiTg&ab_channel=Codemy.com
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_type']

# test --------------------------------------------------------
class UserSignUpForm(UserCreationForm):
#     TYPE_CHOICES = (
#         ('M', 'Member'),
#         ('S', 'Staff'),
#     )
#     user_type = forms.ChoiceField(choices=TYPE_CHOICES)
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'address', 'user_type']
    pass
# -------------------------------------------------------------


class AddClubForm(ModelForm):
    class Meta:
        model = Club
        # name and desc should be required, everything else can be added later
        fields = ['name', 'meet_date', 'location', 'desc']