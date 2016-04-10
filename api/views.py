#Selializers
from __future__ import unicode_literals

from api.model_serializers import PetSerializer, OfferSerializer
from api.model_serializers import RequestSerializer, BreedSerializer, UserSerializer
from api.model_serializers import SizeSerializer

#Models
from api.models import Request, Breed, Offer
from api.models import Pet
from api.models import Size
from django.contrib.auth.models import User

#Django Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin


class RequestViewSet(NestedViewSetMixin, ModelViewSet):
    """
    API endpoint that allows requests to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class PetViewSet(ModelViewSet):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class SizeViewSet(ModelViewSet):

    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class BreedViewSet(ModelViewSet):

    queryset = Breed.objects.all().order_by('name')
    serializer_class = BreedSerializer


class OfferViewSet(NestedViewSetMixin, ModelViewSet):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    # This method uses current user and request for creating new offer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Show all users if is superuser
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)
