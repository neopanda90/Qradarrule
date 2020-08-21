from django.db import models


# Create your models here.

class Qradar(models.Model):
    log_source = models.CharField(max_length=50)
    name = models.TextField()
    condition = models.TextField()
    tactics = models.CharField(max_length=100)
