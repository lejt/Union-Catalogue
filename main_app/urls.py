from django.urls import path   
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # only accessible by staff
    path('members/', views.members_index, name='members_index'),

    # member + staff details page here 
    path('members/<int:member_id>/', views.members_detail, name='members_detail'),
    path('staffs/<int:staff_id>/', views.staffs_detail, name='staffs_detail'),
    path('members/<int:pk>/update/', views.UserUpdate.as_view(), name='members_update'),

    # books related path
    path('books/', views.books_index, name="books"),
    path("rentbook/", views.add_to_rent_books, name="add_to_rent"),
    path('members/<int:member_id>/unassoc_book/<str:book_key>/', views.unassoc_book, name='unassoc_book'),
    
    # club related paths
    path('clubs/', views.clubs_index, name='clubs_index'),
    path('clubs/add_club/', views.add_club, name='add_club'),
    path('clubs/<int:club_id>/', views.clubs_detail, name='clubs_detail'),

    # --------------------------------------------------------------------
    # no login path needed, already built-in
    path('accounts/signup/', views.signup, name='signup'),
    # --------------------------------------------------------------------
    
]