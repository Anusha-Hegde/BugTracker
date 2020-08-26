from django.db import models
import datetime

class Project(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    start = models.DateField(default=datetime.date.today())
    end = models.DateField(blank = True, null = True)
    issues_open = models.IntegerField(null=False, blank=False, default=0)
    total_issues = models.IntegerField(null=False, blank=False, default=0)
    issues_closed = models.IntegerField(null=False, blank=False, default=0)


    def __str__(self):
        return self.name

class Issue(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    # proj = models.On(field='id', to=Project, field_name='id')
    # (Project, on_delete=models.CASCADE, to_field='id')
    proj = models.ForeignKey(Project, to_field='id', on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)

    def __str__(self):
        return self.title
