from django.db import models
import datetime
from django.contrib.auth.models import User, Group

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

class Project(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    start = models.DateField(default=datetime.date.today())
    end = models.DateField(null = True, blank = True)
    issues_open = models.IntegerField(null=False, blank=False, default=0)
    total_issues = models.IntegerField(null=False, blank=False, default=0)
    issues_closed = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name


class Issue(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    user = models.ForeignKey(User, to_field='id', on_delete=models.SET_DEFAULT, default = 1) #default pointing to anonymous user
    project = models.ForeignKey(Project, to_field='id', on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)
    is_open = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title


class Thread(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.SET_DEFAULT, default = 1)
    issue = models.ForeignKey(Issue, to_field='id', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    upvote = models.IntegerField(default=0)


class ProjectMember(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    role = models.ForeignKey(Group, to_field='name', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, to_field='id', on_delete=models.CASCADE)