from django.db import models

# Create your models here.
class  Customer(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    location = models.CharField(max_length=15)
    age = models.IntegerField()
    def __str__(self):
        return self.name.name
class Product(models.Model):
    name = models.CharField(max_length=10)