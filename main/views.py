from django.shortcuts import render
from django.http import HttpResponse
from .models import Users


def indexpage(request):
    return render(request = request, template_name = 'main/index.html')

# , context = {'users': Users.objects.all}
def loginpage(request):
    return render(request = request, template_name = 'main/login.html', context = {'users': Users.objects.all})
