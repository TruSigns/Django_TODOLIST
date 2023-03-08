from django.db import models
#Importing the built-in user models from django
from django.contrib.auth.models import User

# Create your models here.

# this will be my db table
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['complete']