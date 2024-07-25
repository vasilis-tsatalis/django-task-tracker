from django.utils import timezone

from django.db import models
from django.urls import reverse

# Create your models here.

STATUS = (
    ('OPEN', 'OPEN'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('PENDING', 'PENDING'),
    ('CLOSED', 'CLOSED'),
)

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# Projects
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

# Tasks
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='OPEN')
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    notes = models.TextField(null=True, blank=True)
    document = models.FileField(upload_to="project_document/", blank=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
