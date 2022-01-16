from django.urls import path   
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members_index, name='members_index'),
    path('members/<int:member_id>/', views.members_detail, name='members_detail'),

    # # CBV
    # # create
    # path('members/create/', views.MemberInfo.as_view(), name='members_info'),

    # # no login path needed, already built-in
    path('accounts/signup/', views.signup, name='signup'),
]