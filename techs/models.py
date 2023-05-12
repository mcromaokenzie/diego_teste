from django.db import models

# Create your models here.


class Tech(models.Model):
    name = models.CharField(max_length=120, unique=True)
    url = models.URLField(max_length=9999)
    progress = models.IntegerField()
