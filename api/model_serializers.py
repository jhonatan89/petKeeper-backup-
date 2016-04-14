# Django Rest Framework
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

# Models
from api.models import Request, Offer, Pet, Size, Breed, Contact


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name')


class RequestSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Request
        fields = ('id', 'description', 'start_date', 'end_date', 'open', 'request_Pet', 'owner')


class PetSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    size = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())

    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthDate', 'description', 'size', 'breed')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('phone', 'address')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'contact')
        depth = 1


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('phone', 'address')


class OfferSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Offer
        fields = ('description', 'price', 'request', 'user')
