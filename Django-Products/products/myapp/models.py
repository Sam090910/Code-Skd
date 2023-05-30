from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='myapp/images', default="")