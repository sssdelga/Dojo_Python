from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def num_ret(request, val1):
    return HttpResponse(f"placeholder to display blog number: {val1}")

def edit_num(request, val2):
    return HttpResponse(f"placeholder to edit blog {val2}")

def destroy(request, val3):
    # print(val3)
    return redirect('/')

# /int:number/delete - redirect to the "/" route with a method called 
# "destroy"