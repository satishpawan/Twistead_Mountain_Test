from django.db import models
from personal_tasks_project.models import BaseModel

# Create your models here.
class PersonalTask(BaseModel):
    STATUS_CHOICES = (
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    )
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    assigned_to = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="tasks")


    def __str__(self):
        return f"{self.title} {self.assigned_to}"