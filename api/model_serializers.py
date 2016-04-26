# Django Rest Framework
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

# Models
from api.models import Request, Offer, Pet, Size, Breed, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'contact')
        depth = 1


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name')


class RequestSerializer(serializers.ModelSerializer):
    owner = UserShortSerializer(read_only=True)
    request_Pet = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all(), many=True)

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


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('phone', 'address')


class OfferSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)
    request = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    class Meta:
        model = Offer
        fields = ('id', 'description', 'price', 'request', 'accepted', 'user')
