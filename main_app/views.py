from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Staff, User
from .forms import SignUpForm

# from django.contrib.auth.models import User

# from django.views.generic import CreateView

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

# class MemberInfo(CreateView):
#     model = Member
#     fields = ['first_name']


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

# CBV
