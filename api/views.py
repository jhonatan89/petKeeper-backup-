# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import rest_framework
from django.contrib.auth.models import User
from django.core.files import File
from django.db.models import Count
from rest_framework import filters
from rest_framework.decorators import list_route, detail_route
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.filters import RequestFilter
from api.models import Request, Breed, Offer, Size, Pet
from api.serializers import (RequestSerializer, BreedSerializer, SizeSerializer,
                             PetSerializer, OfferSerializer, UserSerializer)
from api.utils import send_petkeeper_email


class RequestViewSet(NestedViewSetMixin, ModelViewSet):
    """
    API endpoint that allows requests to be viewed or edited.
    """
    queryset = Request.objects.annotate(pet_count=Count('pets'), offer_count=Count('offers')).filter(
        open=True).order_by('start_date', 'offer_count', '-pet_count')
    serializer_class = RequestSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RequestFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Request.objects.filter(open=True).exclude(owner=self.request.user).order_by('start_date')

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

    @detail_route(methods=['post'])
    def picture(self, request, pk=None):
        file_obj = File(request.FILES.get('file'))
        pet = self.get_object()
        pet.picture.save('avatar.jpg', file_obj)
        data = '%s' % pet.picture.url
        return Response(data=data)


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
        serializer.save(keeper=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
        # If offer is accepted
        offer = self.get_object()
        if offer.accepted:
            request_obj = Request.objects.get(pk=offer.request.pk)
            request_obj.open = False
            request_obj.save()
            keeper = offer.keeper
            context = {'keeper': keeper, 'request': request_obj, 'offer': offer,
                       'time': request_obj.duration}
            # Send emails context -> info for template, email and template email.
            send_petkeeper_email(context, keeper.email, "conf_keeper_email.html")
            send_petkeeper_email(context, request_obj.owner.email, "conf_owner_email.html")


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        return self.request.user
