from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

app_name = 'main'


def indexpage(request):
    return render(request, 'main/index.html')
    # , context = {'employees': Employee.objects.all}


def homepage(request):
    form = UserCreationForm
    return render(request, 'main/home.html')


def loginpage(request):

    # to avoid going back to login page again and again
    if request.user.is_authenticated:
        return redirect('main:homepage')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username = username, password = password)

            if user:
                login(request, user)
                return redirect('main:homepage')

            else:
                messages.info(request, 'username or password incorrect')
                return redirect('main:loginpage')

    form = UserCreationForm()
    return render(request, 'main/login.html', context={'form':form})

    

def logoutpage(request):
    logout(request)
    return redirect('main:indexpage')


# login_required makes sure user is logged in before viewing the following templates

# @login_required(login_url='main:loginpage')
# def adminpage(request):

# @login_required(login_url='main:loginpage')
# def progmanpage(request):

# @login_required(login_url='main:loginpage')
# def devpage(request):

# @login_required(login_url='main:loginpage')
# def testerpage(request):