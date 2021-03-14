from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

# / --> login and registration form page
# /user/create --> register a new user
# /user/login
# /books --> after valid login/reg

# *******************************************************************
# No user logged in
def index(request):
    return render(request, 'index.html')

def new_user(request):
    errors = User.objects.reg_validate(request.POST)
    email_check = User.objects.filter(email=request.POST['email'])
    if email_check:
        errors['email']='Email already exists in the server'
    if len(errors)>0:
        for k,v in errors.items():
            messages.error(request, v)
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        active_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['user_id']=active_user.id
        return redirect('/books')
    return redirect('/')

def login_user(request):
    email_active = User.objects.filter(email=request.POST['email'])
    if email_active:
        errors = User.objects.login_validate(request.POST)
        if len(errors)>0:
            for k,v, in errors.items():
                messages.error(request, v)
            return redirect('/')
        else:
            active_user = email_active[0]
            if bcrypt.checkpw(request.POST['password'].encode(), active_user.password.encode()):
                request.session['user_id']=active_user.id
                return redirect('/books')
    messages.error(request, 'Invalid user email or password')
    return redirect('/')

# *******************************************************************
# After user logged in
def home(request):
    active_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': active_user,
        'books': Book.objects.all()
    }
    return render(request, 'books_home.html', context)

#/logout
def logout(request):
    request.session.flush()
    return redirect('/')

#/books/create
def create_book(request):
    active_user = User.objects.get(id=request.session['user_id'])
    errors = Book.objects.book_validate(request.POST)
    if len(errors)>0:
        for k,v in errors.items():
            messages.error(request, v)
    else:
        new_book = Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            added_by = active_user,
        )
        new_book.favorites.add(active_user)
    return redirect('/books')

#/books/<int:id>
def view_book(request, book_id):
    active_user = User.objects.get(id=request.session['user_id'])
    active_book = Book.objects.get(id=book_id)
    print(active_book.added_by.__dict__)
    context = {
        'user': active_user,
        'book': active_book
    }
    return render(request, 'book.html', context)

#/books/<int:id>/edit
def edit_book(request, book_id):
    active_book = Book.objects.get(id=book_id)
    active_book.title = request.POST['title']
    active_book.desc = request.POST['desc']
    active_book.save()
    return redirect(f'/books/{book_id}')

#/books/<int:id>/destroy
def delete_book(request, book_id):
    active_book = Book.objects.get(id=book_id)
    active_book.delete()
    return redirect('/books')

#/books/<int:id>/favorite
def fav_book(request, book_id):
    active_user = User.objects.get(id=request.session['user_id'])
    active_book = Book.objects.get(id=book_id)
    active_book.favorites.add(active_user)
    return redirect('/books')

#/books/<int:id>/unfav
def unfav_book(request, book_id):
    active_user = User.objects.get(id=request.session['user_id'])
    active_book = Book.objects.get(id=book_id)
    active_book.favorites.remove(active_user)
    print(active_book.favorites.all)
    return redirect(f'/books/{book_id}')