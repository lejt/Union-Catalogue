from django.urls import path   
from . import views

urlpatterns = [
    # view functions
    path('', views.home, name='home'),
    path('members/', views.members_index, name='members_index'),
    path('books/', views.books_index, name="books"),
    # path('books/<int:books_id>/', views.books_detail, name="books_detail"),
    # path('books/create/', views.BookCreate.as_view(), name='book_create'),

    # path('books/rent/', views.rent_book, name='rent_book'),


    # testing -------------------
    # path("favourite/", views.favourite_page, name = "favourite"),
    # path("add-favourite/", views.add_to_favourite_books, name="add_to_favourite"),
    # path("delete-favourite/<str:id>", views.delete_favourite, name="favourite-delete"),


    path("rentbook/", views.add_to_rent_books, name="add_to_rent"),



    # member + staff details page here - WIP 
    path('members/<int:member_id>/', views.members_detail, name='members_detail'),
    path('staffs/<int:staff_id>/', views.staffs_detail, name='staffs_detail'),
    
    # club related urls
    path('clubs/', views.clubs_index, name='clubs_index'),
    path('clubs/add_club/', views.add_club, name='add_club'),
    path('clubs/<int:club_id>/', views.clubs_detail, name='clubs_detail'),

    # --------------------------------------------------------------------
    # no login path needed, already built-in
    path('accounts/signup/', views.signup, name='signup'),
    # --------------------------------------------------------------------
    
]