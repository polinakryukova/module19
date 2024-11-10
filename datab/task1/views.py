from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game

# from 18.task4
def index_main(request):
    return render(request, 'first_task/main_page.html')

def index_shop(request):
    games = Game.objects.all()
    context = {
        'Games': games
    }
    return render(request, 'first_task/shop.html', context)

def index_trash(request):
    return render(request, 'first_task/trash.html')

def sign_up_by_html(request):

    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18:
            try:
                Buyer.objects.create(name=username, age=age)
                return f"Приветствуем, {username}!"
            except:
                info['error'] = "Пользователь с таким именем уже существует"
        else:
            info['error'] = "Некорректные данные"

        return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    form = UserRegister()
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password:
                try:
                    Buyer.objects.create(name=username, age=age)
                    return f"Приветствуем, {username}!"
                except:
                    info['error'] = "Пользователь с таким именем уже существует"
            else:
                info['error'] = "Пароли не совпадают"
            info['form'] = form
            return render(request, 'first_task/registration_page.html', context=info)

