from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
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


# TESTING -------------------------------------------------------------

def string_list_to_string(string):
      return string.replace("[", "").replace("]", "").replace("\"", "").replace("'", "")

class RentBookForm(ModelForm):
      class Meta:
         model = RentBook
         fields = ['title', 'image', 'author_name', 'key']
         
      def clean(self):
            cleaned_data = super(RentBookForm, self).clean()
            cleaned_data["key"] = string_list_to_string(cleaned_data["key"]).split("/")[-1]
            cleaned_data["title"] = string_list_to_string(cleaned_data["title"])
            cleaned_data["author_name"] = string_list_to_string(cleaned_data["author_name"])
            cleaned_data["image"] = string_list_to_string(cleaned_data["image"])
            return cleaned_data