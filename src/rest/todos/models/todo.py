from django.db import models
from django.contrib.postgres.fields import JSONField

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict, blank=True)