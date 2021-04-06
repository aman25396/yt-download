from django.db import models
from django import forms
# Create your models here.
class Enter(models.Model):
    Input=models.CharField(max_length=200)
    Streams=models.CharField(max_length=200 )

    def __str__(self):
        return self.Input    