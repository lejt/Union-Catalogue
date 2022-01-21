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
    
    path('staffs/<int:staff_id>/schedule/', views.schedule, name='schedule'),
    # path('staffs/schedule/', views.schedule, name='schedule'),

    # books related path
    path('books/', views.books_index, name="books"),
    path("rentbook/", views.add_to_rent_books, name="add_to_rent"),
    path("clubbook/", views.add_to_book_club, name="add_to_book_club"),
    path('members/<int:member_id>/unassoc_book/<str:book_key>/', views.unassoc_book, name='unassoc_book'),

    
    # club related paths
    path('clubs/', views.clubs_index, name='clubs_index'),
    path('clubs/add_club/', views.add_club, name='add_club'),
    path('clubs/<int:club_id>/', views.clubs_detail, name='clubs_detail'),
    path('clubs/<int:club_id>/join_club/', views.join_club, name='join_club'),
    path('clubs/<int:club_id>/delete_club/', views.delete_club, name='delete_club'),
    path('clubs/<int:club_id>/unassoc_memb/<int:member_id>/', views.unassoc_memb, name='unassoc_memb'),
    path('clubs/<int:club_id>/update_club/', views.update_club, name='update_club'),

    # --------------------------------------------------------------------
    # no login path needed, already built-in
    path('accounts/signup/', views.signup, name='signup'),
    # --------------------------------------------------------------------
    
]