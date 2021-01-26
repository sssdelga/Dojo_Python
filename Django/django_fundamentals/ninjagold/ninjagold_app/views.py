from django.shortcuts import render, HttpResponse, redirect

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
        request.session['click_counter']+=1
        if request.session['click_counter']%2 == True:
            request.session['gold_total']+=20
            request.session['activities'].append('Earned 20 golds from Farm')
        else:
            request.session['gold_total'] += 10
            request.session['activities'].append('Earned 10 golds from Farm')
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
        request.session['click_counter']+=1
        if request.session['click_counter']%2 == True:
            request.session['gold_total']+=50
            request.session['activities'].append('Earned 50 golds from Casino')
        else:
            request.session['gold_total'] -= 50
            request.session['activities'].append('Oh no! Lost 50 golds from Casino')
    return redirect('/')

