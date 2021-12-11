from django.db import models

class Service(models.Model):
    name = models.CharField("Service", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Barber(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

