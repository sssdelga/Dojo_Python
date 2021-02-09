from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        desc = request.POST['desc']
    )
    return redirect('/')

def create_ninja(request):
    print('**************')
    print(request.POST)
    dojo_location = Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = dojo_location
    )
    return redirect('/')