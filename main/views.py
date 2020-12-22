from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated, allowed_users
from django.contrib.auth.models import User, Group

from django.views import generic

from .models import Project, Issue, ProjectMember, Tag
import urllib


@unauthenticated
# to avoid going back to login page again and again
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if request.user.groups.exists():
                group = list(
                    request.user.groups.values_list('name', flat=True))
                for i in group:
                    if i == "Admin" or i == "Project Manager" or i == "Developer":
                        return redirect('main:projects')
                    return redirect('main:issues')
            return redirect('main:add_issue')

        messages.info(request, 'username or password incorrect')
        return redirect('main:loginpage')

    form = UserCreationForm()
    return render(request, 'main/login.html', context={'form': form})


# login_required makes sure user is logged in before viewing the following templates
@login_required(login_url='main:loginpage')
@allowed_users(allowed_roles=['Developer', 'Project Manager'])
def projects(request):
    return render(request, 'main/projects.html', context={'projects': Project.objects.all(), 'pro_mem': ProjectMember.objects.all(), 'users': User.objects.all()})


@login_required(login_url='main:loginpage')
@allowed_users(allowed_roles=['Developer', 'Project Manager'])
def issue(request, project_id):
    return render(request, 'main/issue.html', context={'projects': Project.objects.all(), 'pro_mem': ProjectMember.objects.all(), 'issues': Issue.objects.all(), 'project_id': project_id, 'users': User.objects.all()})


@login_required(login_url='main:loginpage')
def issues(request):
    return render(request, 'main/issues.html', context={'projects': Project.objects.all(), 'pro_mem': ProjectMember.objects.all(), 'issues': Issue.objects.all()})


@login_required(login_url='main:loginpage')
def add_issues(request):
    if request.method == 'POST':
        issue = Issue()
        issue.title = request.POST.get('title')
        issue.desc = request.POST.get('desc')
        issue.creator = User.objects.get(id = request.POST.get('creator'))
        issue.assignee = User.objects.get(id = request.POST.get('assignee')) 
        issue.opened = request.POST.get('opened')
        issue.priority = request.POST.get('priority')
        issue.status = request.POST.get('status')
        issue.comment = request.POST.get('comment')
        issue.project = Project.objects.get(id = request.POST.get('project'))

        project = Project.objects.get(id = issue.project.id)
        project.issues_open += 1
        project.total_issues += 1
        project.save()
            
        issue.save()
        issue.tags.add(Tag.objects.get(name = request.POST.get('tags')))

        return render(request, 'main/issues.html', context={'projects': Project.objects.all(), 'pro_mem': ProjectMember.objects.all(), 'issues': Issue.objects.all()})
    return render(request, 'main/add_issue.html', context={'projects': Project.objects.all(), 'tags':Tag.objects.all(), 'users':User.objects.all()})


def logoutpage(request):
    logout(request)
    return redirect('main:loginpage')
