from collections import UserString
from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import AddClubForm, SignUpForm, RentBookForm, UpdateClubForm, ClubBookForm
from django.views.generic.edit import UpdateView
from django.urls import reverse

from main_app.utils import search_books

def home(request):
    return render(request, 'home.html')

# ------------------------ User-related views ------------------------
def members_index(request):
    members = Member.objects.all()
    return render(request, 'user/member_index.html', {'members': members})

def members_detail(request, member_id):
    # original method:
    # member = Member.objects.get(id=member_id)

    # if member is logged in and trying to see their own profile
    if request.user.user_type == 'M':
        # find member_id based on request.user.id (dynamic)
        user = User.objects.get(id=request.user.id)
        member_id = user.member.id

    # if staff is logged in and trying to see other members' profile
    member = Member.objects.get(id=member_id)

    books = member.books.all()

    return render(request, 'user/member_detail.html', {'member': member, 'books':books})

def staffs_detail(request, staff_id):
    # original method:
    # staff = Staff.objects.get(id=user_id)

    user = User.objects.get(id=request.user.id)
    staff_id = user.staff.id

    staff = Staff.objects.get(id=staff_id)
    return render(request, 'user/staff_detail.html', {'staff': staff})

def users_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/user_detail.html', {user})

# ---------------------------------------------------------------------
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            # To access info on the form, request.POST.get('variable name'))
            user = form.save()

            if request.POST.get('user_type') == 'M':
                # for updating a manytomanyfield
                # member = Member.objects.create(user=user)

                # only works if form has a model different than User
                # member = form.save(commit=False)
                # member.user = user
                # member.save()

                member = Member(user=user)
                member.save()

                login(request, user)
                return redirect('members_detail', member.id)

            elif request.POST.get('user_type') == 'S':
                staff = Staff(user=user)
                staff.save()
                login(request, user)
                return redirect('staffs_detail', staff.id)
        else:
            error_message = 'Invalid sign up - try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
# ---------------------------------------------------------------------

def clubs_index(request):
    clubs = Club.objects.all()
    # instantiate addclub form to show in index page
    addclub_form = AddClubForm()
    return render(request, 'clubs/clubs_index.html', {'clubs': clubs, 'addclub_form': addclub_form})

def add_club(request):
    form = AddClubForm(request.POST)
    if form.is_valid():
        new_club = form.save()
        # new_club.save()
        # new_club is like Club.objects.last(), the newest created club should be the last obj
        # new_club id is only available after the .save()
        if request.user.user_type == 'M':
            # find member_id based on request.user.id (dynamic)
            user = User.objects.get(id=request.user.id)
            member_id = user.member.id

        
        # print(Member.objects.get(id=member_id).join_club_date)
        # print(Member.objects.get(id=member_id).create_date)
        # print('2',Member.objects.filter(user=request.user.id)[0].join_club_date)
        # print('2',Member.objects.filter(user=request.user.id)[0].create_date)

        

        # print(Member.objects.get(id=member_id).join_club_date)
        # print(Member.objects.get(id=member_id).create_date)

        # new_club.members.add(Member.objects.get(id=member_id))

        # saving the member here updates the join_club_date to current time
        Member.objects.get(id=member_id).save()

        print(new_club.members.all())
        print(Member.objects.get(id=member_id))
        print(Member.objects.filter(user=request.user.id)[0].id)
        print(Member.objects.filter(id=member_id))
        new_club.members.add(Member.objects.filter(user=request.user.id)[0].id)


        # club = Club.objects.get(id=club_id)
        # club.members.add(user_id)
    else:
        # error_message = 'Invalid club entry - try again'
        print('club form submission failed')
    return redirect('clubs_index')

def clubs_detail(request, club_id):
    club = Club.objects.get(id=club_id)

    # print(club)
    # member_id = Member.objects.filter(user=request.user.id).first().id
    # member = Member.objects.get(id=member_id)

    return render(request, 'clubs/clubs_detail.html', {'club': club})

def join_club(request, club_id):
    club = Club.objects.get(id=club_id)

    # member_id = Member.objects.filter(user=request.user.id)..id
    if request.user.user_type == 'M':
        # find member_id based on request.user.id (dynamic)
        user = User.objects.get(id=request.user.id)
        member_id = user.member.id


    Member.objects.get(id=member_id).save()
    print(club.members.all())
    club.members.add(member_id)
    print(club.members.all())

    return redirect('clubs_detail', club_id=club_id)

def delete_club(request, club_id):
    Club.objects.get(id=club_id).delete()
    return redirect('clubs_index')

def update_club(request, club_id):
    club_to_be_updated = Club.objects.get(id=club_id)

    form = UpdateClubForm(request.POST, instance = club_to_be_updated)
    if form.is_valid():
        form.save()
        # updateclub = form.save()
        # updateclub.save()
        return redirect('clubs_detail', club_id=club_id)
    
    return render(request, 'clubs/clubs_update.html', {'form': form})

def unassoc_memb(request, club_id, member_id):
    # Club.objects.get(id=club_id).members.filter(id=member_id).delete()
    Club.objects.get(id=club_id).members.remove(Member.objects.get(id=member_id))
    return redirect('clubs_detail', club_id=club_id)

def books_index(request):

    # OLD ORIGINAL CODE----------------
    # books = Book.objects.all()

    # if querySearch == request.GET.get("q"):
    #     books = search_books(querySearch)
    #     print(books)
    # return render(request, 'books/index.html', {'books': books})
    # --------------------------------

    books:list = []
    message:str = ""
    # if user search something - get this books, using search_books function
    if searchQuery := request.GET.get("q"):
        books:list[dict] = search_books(searchQuery)
    
        # if we don`t get books we display message
        if len(books) == 0:
                message = "No books was found."
   
    # view raw json data from search query
    # print(books)

    # find clubs members are part of and show them on this page
    if request.user.user_type == 'M':
        # find member_id based on request.user.id (dynamic)
        user = User.objects.get(id=request.user.id)
        member_id = user.member.id
        # print(Club.objects.filter(members=member_id))
        # for club in Club.objects.filter(members=member_id):
        #     print(club.name)
        part_of_clubs = Club.objects.filter(members=member_id)

    return render(request, "books/index.html", {
        "books": books,
        "message":message,
        "part_of_clubs": part_of_clubs
    })

def unassoc_book(request, member_id, book_key):

    # if request.user.user_type == 'M':
    #     # find member_id based on request.user.id (dynamic)
    #     user = User.objects.get(id=request.user.id)
    #     member_id = user.member.id

    RentBook.objects.get(member=member_id, key=book_key).delete()
    return redirect('members_detail', member_id)
    
# Remember, ONETOMANY, One Member has Many RentBook
def add_to_rent_books(request):
    if request.method == "POST":
        # model for RentBookForm is RentBook
        form = RentBookForm(request.POST)
        if form.is_valid():
            # latest rent book added to RentBook Model
            new_rent_book = form.save(commit=False)
    
            if request.user.user_type == 'M':
                # find member_id based on request.user.id (dynamic)
                user = User.objects.get(id=request.user.id)
                member_id = user.member.id

            new_rent_book.member_id = member_id
            new_rent_book.save()

        else:
                print(form.errors)
        
    return redirect('members_detail', member_id=member_id)

def add_to_book_club(request):
    if request.method == "POST":
        form = ClubBookForm(request.POST)
        print('DATA FROM ADD BOOK TO CLUB: ', request.POST)

        if form.is_valid():
            if ('club-selected' not in request.POST):
                return redirect('books')
            new_club_book = form.save(commit=False)
    
            if request.user.user_type == 'M':
                # find member_id based on request.user.id (dynamic)
                user = User.objects.get(id=request.user.id)
                member_id = user.member.id
                # print(Member.objects.get(id=member_id))
                # part_of_clubs = Club.objects.filter(members=member_id)
                # club_id = Member.objects.get(id=member_id).club.id

                club_id = request.POST['club-selected']
                # print('count: ', Club.objects.get(id=club_id).books.count() )

                if (Club.objects.get(id=club_id).books.count() > 0):
                    print('Show previous book: ',Club.objects.get(id=club_id).books.all())
                    Club.objects.get(id=club_id).books.all().delete()
                    print('After clear(): ',Club.objects.get(id=club_id).books.all())


            new_club_book.club_id = club_id
            new_club_book.save()

        else:
                print(form.errors)
        
    return redirect('clubs_detail', club_id=club_id)

class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'address']
    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse('members_detail', kwargs={'member_id': self.object.id},)
        
        


  



    







   
    



    
 
    