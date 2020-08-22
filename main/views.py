from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated




@unauthenticated
# to avoid going back to login page again and again
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username = username, password = password)

        if user:
            login(request, user)
            return redirect('main:indexpage')

        messages.info(request, 'username or password incorrect')
        return redirect('main:loginpage')


    form = UserCreationForm()
    return render(request, 'main/login.html', context={'form':form})

    

def logoutpage(request):
    logout(request)
    return redirect('main:loginpage')


# login_required makes sure user is logged in before viewing the following templates
@login_required(login_url='main:loginpage')
def indexpage(request):
    group = list(request.user.groups.values_list('name',flat = True))
    return render(request, 'main/index.html', context={'group':group})


@login_required(login_url='main:loginpage')
def adminpage(request):
    return render(request, 'main/admin.html')


@login_required(login_url='main:loginpage')
def anypage(request):
    return render(request, 'main/any.html')