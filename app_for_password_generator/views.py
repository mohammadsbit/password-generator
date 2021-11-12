from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'app_for_password_generator/home.html')


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    final = ''
    for i in range(10):
       final += random.choice(chars)
    return render(request, 'app_for_password_generator/password.html', {'password': final})

def about(request):
    return render(request, 'app_for_password_generator/about.html')
