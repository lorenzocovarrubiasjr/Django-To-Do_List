from django.contrib import admin
from .models import TodoItem, TodoList

# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(TodoList, TodoListAdmin)

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("done","content","todo_list")
    
admin.site.register(TodoItem, TodoItemAdmin)
