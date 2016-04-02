#Django Rest Framework
from rest_framework import serializers

#Models
from api.models import Request
from api.models import Pet
from api.models import Size


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'description', 'start_date', 'end_date', 'open')


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'birthDate', 'description', 'size', 'breed')


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('name')