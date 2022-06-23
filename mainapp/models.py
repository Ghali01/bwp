from operator import mod
from django.db import models

class Item(models.Model):
    name=models.CharField(max_length=255)
    url=models.URLField()
    image=models.ImageField(upload_to='items/')
    type=models.CharField(max_length=1)
