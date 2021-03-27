from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Blog(models.Model):
    title = models.CharField(null=False, blank=False, max_length=256)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # 1: Django 101
        return f"{self.id}: {self.title}"
