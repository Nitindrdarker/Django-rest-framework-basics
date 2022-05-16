from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title