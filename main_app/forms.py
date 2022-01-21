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

class AddClubForm(ModelForm):
    class Meta:
        model = Club
        # name and desc should be required, everything else can be added later
        fields = ['name', 'meet_date', 'location', 'desc']

class UpdateClubForm(ModelForm):
    class Meta:
        model = Club
        exclude = ('create_date',)
        fields = ['meet_date', 'location', 'desc']

# Data from books api -------------------------------------------------------------

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

class ClubBookForm(ModelForm):
      class Meta:
         model = ClubBook
         fields = ['title', 'image', 'author_name', 'key']
         
      def clean(self):
            cleaned_data = super(ClubBookForm, self).clean()
            cleaned_data["key"] = string_list_to_string(cleaned_data["key"]).split("/")[-1]
            cleaned_data["title"] = string_list_to_string(cleaned_data["title"])
            cleaned_data["author_name"] = string_list_to_string(cleaned_data["author_name"])
            cleaned_data["image"] = string_list_to_string(cleaned_data["image"])
            return cleaned_data

# class DaySelect(forms.Select):
#     def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
#         option = super().create_option(name, value, label, selected, index, subindex, attrs)
#         return option

# class ShiftSelect(forms.Select):
#     def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
#         option = super().create_option(name, value, label, selected, index, subindex, attrs)
#         return option

# class ScheduleForm(ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['day', 'shift'] 
        # widgets = {'day': DaySelect, 'shift': ShiftSelect}

class ScheduleForm(ModelForm):
    class Meta:
        model = Shift
        fields = ['day', 'shift'] 