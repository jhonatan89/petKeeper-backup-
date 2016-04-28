# Selializers
from __future__ import unicode_literals

import rest_framework
from api.model_serializers import PetSerializer, OfferSerializer
from api.model_serializers import RequestSerializer, BreedSerializer, UserSerializer, ContactSerializer
from api.model_serializers import SizeSerializer

# Models
from api.models import Request, Breed, Offer, Contact
from api.models import Pet
from api.models import Size
from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.decorators import list_route
from rest_framework import status


class RequestViewSet(NestedViewSetMixin, ModelViewSet):
    """
    API endpoint that allows requests to be viewed or edited.
    """
    queryset = Request.objects.filter(open=True).order_by('start_date')
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @list_route()
    def me(self, request):
        my_requests = Request.objects.filter(owner=request.user).order_by('start_date')
        data = self.get_serializer(my_requests, many=True).data
        return Response(data)


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Pet.objects.filter(user=self.request.user)


class PetRequestViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class SizeViewSet(ReadOnlyModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class BreedViewSet(ReadOnlyModelViewSet):
    queryset = Breed.objects.all().order_by('name')
    serializer_class = BreedSerializer


class OfferViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    # This method uses current user and request for creating new offer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        if self.request.POST['accepted']:
            request_obj = Request.objects.get(pk=self.request.POST['request'])
            request_obj.open = False
            request_obj.save()


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeView(APIView):
    queryset = User.objects.all()
    permission_classes = [rest_framework.permissions.AllowAny]

    def get(self, request, format=None):
        return Response(UserSerializer(request.user).data)

    def post(self, request, format=None):
        contact = Contact.objects.get(user=request.user)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
