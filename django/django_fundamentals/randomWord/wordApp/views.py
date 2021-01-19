from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def rand_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['word'] = get_random_string(length=14)
    request.session['count'] += 1
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')






# def index(request):
#     if request.method == 'GET':
#         print('RANDOM STRING VIA GET REQUEST!')
#         request.session['counter'] = 1
#     if request.method == 'POST':
#         print('RANDOM STRING VIA POST REQUEST')
#         request.session['counter'] += 1
#     random_string = get_random_string(length=14)
#     context = {
#         'string' : random_string
#     } 
#     return render(request, 'index.html', context)

# def reset(request):
#     print('STRING COUNTER RESET')
#     request.session.flush()
#     return redirect('/')