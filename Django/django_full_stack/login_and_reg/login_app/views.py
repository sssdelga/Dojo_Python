from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# ?:Don't allow a user who is not logged in to reach the /success route (i.e. by making a GET request in the address bar)

def index(request):
    return render(request, 'index.html')
    
def register(request):
    errors=User.objects.reg_validate(request.POST)
    email_check = User.objects.filter(email=request.POST['email'])
    if email_check:
        errors['email']='Email already exists in the server'
    if len(errors)>0:
        for k,v in errors.items():
            messages.error(request,v)
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        active_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['user_id']=active_user.id
        return redirect('/success')
    return redirect('/')

def login(request):
    errors=User.objects.login_validate(request.POST)
    email_check = User.objects.filter(email=request.POST['email'])
    if email_check:
        if len(errors)>0:
            for k,v in errors.items():
                messages.error(request,v)
            return redirect('/')
        else:
            active_user = email_check[0]
            if bcrypt.checkpw(request.POST['password'].encode(), active_user.password.encode()):
                print('validated user')
                request.session['user_id']=active_user.id
                return redirect('/success')
    messages.error(request,'Invalid user')
    return redirect('/')

def success(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login_success.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')