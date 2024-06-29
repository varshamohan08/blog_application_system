from django.db import models
from django.contrib.auth.models import User

# Create your models here. title, content, publication date, and author
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='created_notes', on_delete=models.CASCADE)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title