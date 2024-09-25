from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import UserRegister
from .models import *

# Create your views here.
def platform(request):
    return render(request, 'platform.html')

def games(request):
    context = {
        'title': 'Игры',
        'game_list': Game.objects.all()
    }
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')

def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {'error': []}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'].append('Пароли не совпадают')
        if age < 18:
            info['error'].append('Вы должны быть старше 18')
        for user in users:
            if username == user.name:
                info['error'].append('Пользователь уже существует')
                break
        if not info['error']:
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Приветствуем, {username}!')

    context = {'errors': info['error']}
    return render(request, 'registration_page.html', context)

def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {'error': []}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if password != repeat_password:
                info['error'].append('Пароли не совпадают')
            if age < 18:
                info['error'].append('Вы должны быть старше 18')
            for user in users:
                if username == user.name:
                    info['error'].append('Пользователь уже существует')
                    break
            if not info['error']:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    context = {'form': form, 'errors': info['error']}
    return render(request, 'registration_page.html', context)