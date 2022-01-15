from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'registration/signup.html')

def member_signup(request):
    return render(request, 'registration/member_signup.html')

def staff_signup(request):
    return render(request, 'registration/staff_signup.html')
