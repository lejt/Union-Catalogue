from django.urls import path   
from . import views

urlpatterns = [
    # view functions
    path('', views.home, name='home'),
    path('members/', views.members_index, name='members_index'),
    path('members/<int:member_id>/', views.members_detail, name='members_detail'),
    path('staffs/<int:staff_id>/', views.staffs_detail, name='staffs_detail'),
    
    path('clubs/', views.clubs_index, name='clubs_index'),

    # CBV
    # path('clubs/', views.ClubList.as_view(), name='clubs_index'),


    # no login path needed, already built-in
    path('accounts/signup/', views.signup, name='signup'),
]