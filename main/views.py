from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated

app_name = 'main'



@unauthenticated
# to avoid going back to login page again and again
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username = username, password = password)

        if user:
            group = list(user.groups.values_list('name',flat = True))

            if 'Admin' in group:
                login(request, user)
                return redirect('main:adminpage')

            elif 'Project Manager' in group:
                login(request, user)
                return redirect('main:pmpage')
            
            elif 'Developer' in group:
                login(request, user)
                return redirect('main:devpage')

            elif 'Tester' in group:
                login(request, user)
                return redirect('main:testerpage')

        messages.info(request, 'username or password incorrect')
        return redirect('main:loginpage')


    form = UserCreationForm()
    return render(request, 'main/login.html', context={'form':form})

    

def logoutpage(request):
    logout(request)
    return redirect('main:loginpage')


# login_required makes sure user is logged in before viewing the following templates

@login_required(login_url='main:loginpage')
def adminpage(request):
    return render(request, 'main/admin.html')

@login_required(login_url='main:loginpage')
def pmpage(request):
    return render(request, 'main/pm.html')

@login_required(login_url='main:loginpage')
def devpage(request):
    return render(request, 'main/dev.html')

@login_required(login_url='main:loginpage')
def testerpage(request):
    return render(request, 'main/tester.html')

# , context={'user':request.user}