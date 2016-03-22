from rest_framework import serializers
from api.models import Request


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'description', 'start_date', 'end_date', 'open')