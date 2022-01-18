from django.urls import path   
from . import views

urlpatterns = [
    # view functions
    path('', views.home, name='home'),
    path('members/', views.members_index, name='members_index'),
    path('members/<int:member_id>/', views.members_detail, name='members_detail'),
    path('books/', views.books_index, name="books"),
    path('books/<int:books_id>/', views.books_detail, name="books_detail"),
    path('staffs/<int:staff_id>/', views.staffs_detail, name='staffs_detail'),
    
    path('clubs/', views.clubs_index, name='clubs_index'),
    path('clubs/add_club/', views.add_club, name='add_club'),

    # CBV
    # path('clubs/create/', views.ClubCreate.as_view(), name='clubs_create'),


    # no login path needed, already built-in
    path('accounts/signup/', views.signup, name='signup'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    
]