# others
from __future__ import unicode_literals
# Django
from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


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


def upload_to_pet(instance, filename):
    return '/'.join([
        'user',
        '%d' % instance.user.pk,
        'pets',
        '%d' % instance.pk,
        '%s' % filename])


def upload_to_profile(instance, filename):
    return '/'.join([
        'user',
        '%d' % instance.user.pk,
        '%s' % filename])


class Pet(models.Model):
    name = models.CharField(max_length=30)
    birthDate = models.DateField()
    description = models.CharField(max_length=400, null=True, blank=True)
    size = models.ForeignKey(Size)
    breed = models.ForeignKey(Breed)
    user = models.ForeignKey(User, default=1)
    picture = models.ImageField('logo', upload_to=upload_to_pet, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.name


class Request(models.Model):
    description = models.CharField(max_length=400, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    open = models.BooleanField(default=False)
    request_Pet = models.ManyToManyField(Pet)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return '%s' % self.description


class Offer(models.Model):
    description = models.CharField(max_length=400)
    price = models.FloatField()
    keeper = models.ForeignKey(User)
    request = models.ForeignKey(Request)
    accepted = models.NullBooleanField()

    def __unicode__(self):
        return '%s' % self.description


class Contact(models.Model):
    user = models.OneToOneField(User, related_name='contact')
    phone = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=50, null=True)
    picture = models.ImageField('logo', upload_to=upload_to_profile, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.user


def add_to_default_group(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user.contact = Contact()
        user.contact.save()
        group = Group.objects.get(name='users')
        user.groups.add(group)
        Contact.objects.get_or_create(user=user)


post_save.connect(add_to_default_group, sender=User)
