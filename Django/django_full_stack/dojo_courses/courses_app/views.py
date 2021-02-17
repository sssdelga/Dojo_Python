from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create_course(request):
    errors=Course.objects.basic_validator(request.POST)
    if len(errors)>0:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('/')

    Course.objects.create(
        name = request.POST['name'],
        desc = request.POST['desc']
    )
    return redirect('/')

def confirm_delete(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'confirm_delete.html', context)

def delete_course(request, id):
    delete_dis = Course.objects.get(id=id)
    delete_dis.delete()
    return redirect('/')