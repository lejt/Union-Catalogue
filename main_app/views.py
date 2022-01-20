from collections import UserString
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import *
from .forms import AddClubForm, SignUpForm, UserSignUpForm, RentBookForm

from django.views.generic.edit import  DeleteView


# from django.views.generic import ListView

from main_app.utils import search_books



    # def get_succes_url(self):
    #     return reverse() 
# def unassoc_book(request, book_key, member_id):
#     print(Member.objects.get(id=member_id).books.key[1])
# #   Member.objects.get(id=member_id).books.key[1].remove(books.key[1]==book_key)
#     return redirect('members_detail', member_id=member_id)


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

        new_club.members.add(Member.objects.filter(user=request.user.id)[0].id)

        # club = Club.objects.get(id=club_id)
        # club.members.add(user_id)
    else:
        # error_message = 'Invalid club entry - try again'
        print('club form submission failed')
    return redirect('clubs_index')

def clubs_detail(request, club_id):
    club = Club.objects.get(id=club_id)
    return render(request, 'clubs/clubs_detail.html', {'club': club})

# CBV
# class BookCreate(CreateView):
#     model = Book
#     fields = '__all__'

# def books_detail(request, books_id):
#     book = Book.objects.get(id=books_id)
#     return render(request, 'books/detail.html', {'book':book})

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
    
    # print('PRINT BOOKS', books)



    print(Member.objects.get(id=member_id).books.key[1])
    return render(request, "books/index.html", {
        "books": books,
        "message":message
    })

# def rent_book(request):
    # member = Member.objects.get(id=member_id)
    # member.books.add(book_key)
    # return redirect('books/index')

    # if request.method == "POST":
    #     data = dict(request.POST)
    #     data['user'] = request.user
    #     form = FavouriteBookForm(data)
    #     if form.is_valid():
    #             form.save()
    #     else:
    #             print(form.errors)
        

    # return redirect(reverse('books/index'))

def favourite_page(request):
      message:str = ""
      queryset = request.user.books.all()
      if len(queryset) == 0:
            message = "You don`t have favourite books yet"
      return render(request, "books/favourite.html", {"books":queryset, "message":message})

# def add_to_favourite_books(request):
#       if request.method == "POST":
#             data = dict(request.POST)
#             data['user'] = request.user
#             form = FavouriteBookForm(data)

#             if form.is_valid():
#                     form.save()
#             else:
#                     print(form.errors)
            
#             return redirect(reverse("books/index"))
#       return redirect(reverse("books/index"))
    
# Remember, ONETOMANY, One Member has Many RentBook
def add_to_rent_books(request):
    if request.method == "POST":
        # model for RentBookForm is RentBook
        form = RentBookForm(request.POST)
        print('form HERE: ', form)
        if form.is_valid():
            # latest rent book added to RentBook Model
            new_rent_book = form.save(commit=False)
    
            if request.user.user_type == 'M':
                # find member_id based on request.user.id (dynamic)
                user = User.objects.get(id=request.user.id)
                member_id = user.member.id
            # member = Member.objects.get(id=member_id)

            new_rent_book.member_id = member_id
            new_rent_book.save()

            print('I rent out the book with my id: ',new_rent_book.member_id)
            print('This is my new book: ', new_rent_book)
            print('Member.books.all: ', Member.objects.get(id=member_id).books.all())

        else:
                print(form.errors)
        
    return redirect('members_detail', member_id=member_id)
      

# def delete_favourite(request, id):
#       try:
#             FavouriteBook.objects.get(user = request.user, key = id).delete()
#       except FavouriteBook.DoesNotExist:
#             pass
      
#       return redirect("books:favourite")