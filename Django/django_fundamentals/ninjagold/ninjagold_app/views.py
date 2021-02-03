from django.shortcuts import render, HttpResponse, redirect

import random

def index(request):
    if 'gold_total' not in request.session:
        request.session['gold_total']=0
    if 'click_counter' not in request.session:
        request.session['click_counter']=0
    if 'activities' not in request.session:
        request.session['activities']=[]
    else:
        print(request.session['gold_total'])
    return render(request, 'index.html')

def process(request, place):
    if place == 'Farm':
        x = random.randint(10, 20)
        request.session['gold_total']+=x
        request.session['activities'].append(f'Earned {x} golds from Farm')
    if place == 'Cave':
        request.session['click_counter']+=1
        if request.session['click_counter']%2 == True:
            request.session['gold_total']+=5
            request.session['activities'].append('Earned 5 golds from Cave')
        else:
            request.session['gold_total'] += 10
            request.session['activities'].append('Earned 10 golds from Cave')
    if place == 'House':
        request.session['click_counter']+=1
        if request.session['click_counter']%2 == True:
            request.session['gold_total']+=2
            request.session['activities'].append('Earned 2 golds from House')
        else:
            request.session['gold_total'] += 5
            request.session['activities'].append('Earned 5 golds from House')
    if place == 'Casino':
        w = random.randint(-50,50)
        request.session['gold_total']+=w
        if w < 0:
            request.session['activities'].append((f'Oh no! Lost {abs(w)} golds from Casino','red'))
        
        else:
            request.session['activities'].append((f'Earned {w} from Casino','green'))
    return redirect('/')

