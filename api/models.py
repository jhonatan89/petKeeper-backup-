# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from uuid import uuid4

from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_to_pet(instance, filename):
    return '/'.join([
        'user',
        '%d' % instance.user.pk,
        'pets',
        '%s.jpg' % uuid4()])


def upload_to_profile(instance, filename):
    return '/'.join([
        'user',
        '%d' % instance.user.pk,
        '%s' % filename])


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
    description = models.CharField(max_length=400, null=True, blank=True)
    size = models.ForeignKey(Size)
    breed = models.ForeignKey(Breed)
    user = models.ForeignKey(User, default=1)
    picture = models.ImageField('picture', upload_to=upload_to_pet, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.name


class Request(models.Model):
    description = models.CharField(max_length=400, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    open = models.BooleanField(default=False)
    pets = models.ManyToManyField(Pet)
    owner = models.ForeignKey(User, related_name='requests')

    def __unicode__(self):
        return '%s' % self.description

    @property
    def duration(self):
        return (self.end_date - self.start_date).days


class Offer(models.Model):
    description = models.CharField(max_length=400)
    price = models.FloatField()
    keeper = models.ForeignKey(User, related_name='offers')
    request = models.ForeignKey(Request, related_name='offers')
    accepted = models.NullBooleanField()

    def __unicode__(self):
        return '%s' % self.description


class Contact(models.Model):
    user = models.OneToOneField(User, related_name='contact')
    phone = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField('picture', upload_to=upload_to_profile, null=True, blank=True)
    about = models.TextField(max_length=400, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.user


@receiver(post_save, sender=User)
def add_to_default_group(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        Contact.objects.get_or_create(user=user)
        if not user.is_superuser:
            group = Group.objects.get(name='users')
            user.groups.add(group)
