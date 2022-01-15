from django.urls import path   
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/member', views.member_signup, name='member_signup'),
    path('accounts/signup/staff', views.staff_signup, name='staff_signup'),
]