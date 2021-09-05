from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    datetime = models.DateTimeField(blank=True)
    description = models.TextField(max_length=500)