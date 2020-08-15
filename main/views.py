from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Employee
from django.contrib.auth import login, logout

app_name = 'main'


def indexpage(request):
    return render(request = request, template_name = 'main/index.html')


def loginpage(request):
    return render(request = request, template_name = 'main/login.html')
    # , context = {'employees': Employee.objects.all}

def logoutpage(request):
    logout(request)
    return redirect('main: indexpage')