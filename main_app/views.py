from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import AddClubForm, SignUpForm

# from django.contrib.auth.models import User

from django.views.generic.edit import CreateView
# from django.views.generic import ListView

# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your views here.
def home(request):
    return render(request, 'home.html')

def members_index(request):
    members = Member.objects.all()
    return render(request, 'user/member_index.html', {'members': members})

def members_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    return render(request, 'user/member_detail.html', {'member': member})

def staffs_detail(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    return render(request, 'user/staff_detail.html', {'staff': staff})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = SignUpForm(request.POST)
        if form.is_valid():
            # This will add the user to the database

            # To access info on the form, request.POST.get('variable name'))
            user = form.save()

            # This is how we log a user in via code
            # login(request, user)
            if request.POST.get('user_type') == 'M':
                # member = Member.objects.create_user(user=user)
                # member.user_id = user.id
                # print(member.user_id)

                # user = form.save()

                user_memb = Member(user_memb=user)
                user_memb.save()
                login(request, user)

                # return redirect('home')
                # return redirect('members_index')
                return redirect('members_detail', user_memb.id)

            elif request.POST.get('user_type') == 'S':
                user_staff = Staff(user_staff=user)
                user_staff.save()
                login(request, user)
                return redirect('staffs_detail', user_staff.id)

            # return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def clubs_index(request):
    clubs = Club.objects.all()
    # instantiate addclub form to show in index page
    addclub_form = AddClubForm()
    return render(request, 'clubs/clubs_index.html', {'clubs': clubs, 'addclub_form': addclub_form})

def add_club(request):
    print('-------added')
    form = AddClubForm(request.POST)
    print('-------', request.POST)
    print(form)
    if form.is_valid():
        print('valid')
        new_club = form.save()
        # new_club.save()
        # clubs = Club.objects.all()
    else:
        print('--------form invalid')
    # return render(request, 'clubs/clubs_index.html, {'clubs': clubs})
    return redirect('clubs_index')

# CBV
# class ClubCreate(CreateView):
#     model = Clubs
#     fields = ['name', 'desc']

#     def get(self, request):
#         return render(request, 'clubs/clubs_index.html')