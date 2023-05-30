from django.db import models

# Create your models here.
class file(models.Model):
    name = models.CharField(max_length=50, default='N/A')
    ob = models.FileField(upload_to='fd/images')