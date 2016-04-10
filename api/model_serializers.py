# Django Rest Framework
from __future__ import unicode_literals
from rest_framework import serializers
from django.contrib.auth.models import User

# Models
from api.models import Request, Offer
from api.models import Pet
from api.models import Size
from api.models import Breed


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name')


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'description', 'start_date', 'end_date', 'open')


class PetSerializer(serializers.HyperlinkedModelSerializer):
    breed = BreedSerializer()
    size = SizeSerializer()

    class Meta:
        model = Pet
        fields = ('name', 'birthDate', 'description', 'size', 'breed')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # pets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())
    # offers = serializers.PrimaryKeyRelatedField(many=True, queryset=Offer.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class OfferSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Offer
        fields = ('description', 'price', 'request', 'user')
