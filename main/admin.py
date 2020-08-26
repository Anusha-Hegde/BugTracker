from django.contrib import admin
from .models import Project, Issue

# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)