from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def to_d(self):
        return {"name": self.name, "description": self.description}
        
class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    content = models.TextField()
    done = models.BooleanField(default=False)
    
    def to_d(self):
        return {"todo_list": self.todo_list, "content":self.content, "done":self.done}