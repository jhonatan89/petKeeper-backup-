# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Request, Offer, Pet, Size, Breed, Contact


class ContactShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('phone', 'address', 'picture', 'about')


class UserSerializer(serializers.ModelSerializer):
    contact = ContactShortSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'contact')
        read_only_fields = ('id', 'username', 'email', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        # Only the contact information is updated
        contact_data = validated_data.get('contact')
        contact = instance.contact
        for attr, value in contact_data.items():
            setattr(contact, attr, value)
        contact.save()
        return instance


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name')


class PetNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthDate', 'description', 'size', 'breed', 'picture')
        read_only_fields = ('name', 'birthDate', 'description', 'size', 'breed', 'picture')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}


class RequestSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    pets = PetNestedSerializer(many=True)

    class Meta:
        model = Request
        fields = ('id', 'description', 'start_date', 'end_date', 'open', 'pets', 'owner')

    def create(self, validated_data):
        pets = validated_data.pop('pets')
        request = Request.objects.create(**validated_data)
        for pet in pets:
            tmp = Pet.objects.get(pk=pet.get('id'))
            request.pets.add(tmp)
        return request


class PetSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    size = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())

    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthDate', 'description', 'size', 'breed', 'picture')


class OfferSerializer(serializers.ModelSerializer):
    keeper = UserSerializer(read_only=True)
    request = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    class Meta:
        model = Offer
        fields = ('id', 'description', 'price', 'request', 'accepted', 'keeper')
