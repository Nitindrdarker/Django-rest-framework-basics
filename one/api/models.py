from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=225)
    comleted = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        return self.title