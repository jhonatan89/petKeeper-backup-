from api.model_serializers import RequestSerializer
from api.models import Request
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
