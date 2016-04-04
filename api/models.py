#others
from __future__ import unicode_literals
#Django
from django.contrib.auth.models import User
from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=30)

    class Meta(object):
        ordering = ('name',)

    def __unicode__(self):
        return '%s' % self.name


class Size(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return '%s' % self.name


class Pet(models.Model):
    name = models.CharField(max_length=30)
    birthDate = models.DateField()
    description = models.CharField(max_length=400)
    size = models.ForeignKey(Size)
    breed = models.ForeignKey(Breed)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return '%s' % self.name


class Request(models.Model):
    description = models.CharField(max_length=400)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    open = models.BooleanField(default=False)
    request_Pet = models.ManyToManyField(Pet)

    def __unicode__(self):
        return '%s' % self.description


class Offer(models.Model):
    description = models.CharField(max_length=400)
    price = models.FloatField()
    user = models.ForeignKey(User)
    request = models.ForeignKey(Request)

    def __unicode__(self):
        return '%s' % self.description

