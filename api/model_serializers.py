# Django Rest Framework
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

# Models
from api.models import Request, Offer, Pet, Size, Breed, Contact


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'description', 'start_date', 'end_date', 'open', 'request_Pet')
        depth = 1


class PetSerializer(serializers.HyperlinkedModelSerializer):
    breed = BreedSerializer()
    size = SizeSerializer()

    class Meta:
        model = Pet
        fields = ('name', 'birthDate', 'description', 'size', 'breed')


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
