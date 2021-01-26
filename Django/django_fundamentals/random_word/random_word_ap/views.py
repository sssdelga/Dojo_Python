from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['word']=get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter']=1
    return render(request, 'index.html')

def count(request):
    request.session['counter']=request.session['counter']+1
    return redirect('/random_word')

def reset(request):
    request.session['counter']=1
    return redirect('/random_word')