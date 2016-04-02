from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=30)


class Size(models.Model):
    SIZE_CHOICES = (
        ('XS', 'X-Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('G', 'Giant'),
    )
    name = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')


class Pet(models.Model):
    name = models.CharField(max_length=30)
    birthDate = models.DateField()
    description = models.CharField(max_length=400)
    size = models.ForeignKey(Size)
    breed = models.ForeignKey(Breed)


class Request(models.Model):
    description = models.CharField(max_length=400)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    open = models.BooleanField(default=False)
    request_Pet = models.ManyToManyField(Pet)


class Offer(models.Model):
    description = models.CharField(max_length=400)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request)



