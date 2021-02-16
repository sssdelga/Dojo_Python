from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new_show(request):
    if request.method=='GET':
        return render(request, 'new_show.html')
    else:
        errors = Show.objects.basic_validator(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/shows/new')
        else:
            Show.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                description = request.POST['description']
            )
            return redirect('/shows')

def view_show(request, show_id):
    context ={
        'show': Show.objects.get(id=show_id)
    }
    
    return render(request, 'show_id.html', context)

def edit_show(request, show_id):
    if request.method=='GET':
        context = {
            'show': Show.objects.get(id=show_id)
        }
        return render(request, 'edit_show.html', context)
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/shows/<int:show_id>/edit')
        else:
            edit = Show.objects.get(id=show_id)
            print(edit)
            if edit.title == True:
                edit.title = request.POST['title']

            if edit.network == True:
                edit.network = request.POST['network']

            if edit.release_date == True:
                edit.release_date = request.POST['release_date']

            if edit.description == True:
                edit.description = request.POST['description']
            
            messages.success(request, 'Show successfully updated')
            return redirect('/shows/<int:show_id>')

def delete_show(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')