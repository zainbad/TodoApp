from django.contrib import admin

# Register your models here.
from . models import *


class Todo_listAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'user')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'todo_list', 'created', 'modified')

admin.site.register(Todo_list, Todo_listAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(User_Profile)