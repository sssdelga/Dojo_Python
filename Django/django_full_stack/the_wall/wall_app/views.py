from django.shortcuts import render, redirect
from wall_app.models import Message, Comment
from login_app.models import User

#wall/home
#wall/all
#wall/create
#wall/comment/create

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    print('*****************entered wall')
    context = {
        'wall_messages': Message.objects.all().order_by('-created_at'),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'wall.html', context)

def wall_create(request):
    active_user = User.objects.get(id=request.session['user_id'])
    Message.objects.create(
        author = active_user,
        message_content=request.POST['message_content']
    )
    return redirect('/wall/home')

def wall_detail(request):
    context = {
        'wall_messages': Message.objects.all().order_by('-created_at'),
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'wall_detail.html', context)

def comment_create(request, mess_id):
    active_user = User.objects.get(id=request.session['user_id'])
    message_id = Message.objects.get(id=mess_id)
    Comment.objects.create(
        author = active_user,
        message = message_id,
        comment_content = request.POST['comment_content']
    )
    return redirect('/wall/all')