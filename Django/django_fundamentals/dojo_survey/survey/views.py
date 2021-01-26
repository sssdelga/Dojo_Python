from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        request.session['ur_name']=request.POST['ur_name']
        request.session['dojo_location']= request.POST['dojo_location']
        request.session['fav_lang']= request.POST['fav_lang']
        request.session['comments']= request.POST['comments']
        
        return redirect('/process')
    return redirect('/')

def process(request):
    return render(request, 'result.html')

