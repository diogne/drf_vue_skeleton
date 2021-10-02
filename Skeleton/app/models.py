from django.db import models

# Create your models here.

class BasicModel(models.Model):
    """model de base pour le skelette"""
    word = models.CharField(max_length=50)
