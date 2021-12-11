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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=True)
    subject = models.CharField(max_length=150, null=True)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    message = models.TextField()


class Post(models.Model):
    name = models.CharField(max_length=150, null=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=160, unique=True)
    service = models.ForeignKey(Service, verbose_name="service", on_delete=models.CASCADE)



