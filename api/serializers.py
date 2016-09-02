from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

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


class PetNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthDate', 'description', 'size', 'breed', 'picture')
        read_only_fields = ('name', 'birthDate', 'description', 'size', 'breed', 'picture')
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}


class RequestSerializer(serializers.ModelSerializer):
    owner = UserShortSerializer(read_only=True)
    request_Pet = PetNestedSerializer(many=True)

    class Meta:
        model = Request
        fields = ('id', 'description', 'start_date', 'end_date', 'open', 'request_Pet', 'owner')

    def create(self, validated_data):
        pets = validated_data.pop('request_Pet')
        request = Request.objects.create(**validated_data)
        for pet in pets:
            tmp = Pet.objects.get(pk=pet.get('id'))
            request.request_Pet.add(tmp)
        return request


class PetSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    size = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())

    class Meta:
        model = Pet
        fields = ('id', 'name', 'birthDate', 'description', 'size', 'breed', 'picture')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('phone', 'address', 'picture', 'about')
        read_only_fields = ('picture',)


class OfferSerializer(serializers.ModelSerializer):
    keeper = UserSerializer(read_only=True)
    request = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    class Meta:
        model = Offer
        fields = ('id', 'description', 'price', 'request', 'accepted', 'keeper')