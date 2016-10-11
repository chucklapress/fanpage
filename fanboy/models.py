from django.db import models

# Create your models here.
class BriarPipe(models.Model):
    shape = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    groupsize = models.IntegerField()
    craftsman = models.CharField(max_length=40)
