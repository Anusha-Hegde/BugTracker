from django.contrib import admin
from .models import Project, Issue, Tag, ProjectMember

# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Issue)
admin.site.register(ProjectMember)