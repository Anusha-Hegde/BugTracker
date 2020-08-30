from django.contrib import admin
from .models import Project, Issue, Thread, Tag, ProjectMember

# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Issue)
admin.site.register(Thread)
admin.site.register(ProjectMember)