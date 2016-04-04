#Selializers
from api.model_serializers import RequestSerializer, BreedSerializer
from api.model_serializers import PetSerializer, OfferSerializer
from api.model_serializers import SizeSerializer

#Models
from api.models import Request, Breed, Offer
from api.models import Pet
from api.models import Size

#Django Rest Framework
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    # This method provide url_path='request/me'
    @list_route(methods=['get'], url_path='me')
    def me(self, request):
        return Response({})


class PetViewSet(viewsets.ModelViewSet):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class SizeViewSet(viewsets.ModelViewSet):

    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class BreedViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all().order_by('name')
    serializer_class = BreedSerializer


class OfferViewSet(viewsets.ModelViewSet):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    # This method returns the current user offers
    def get_queryset(self):
        offers_by_user = Offer.objects.filter(user=self.request.user)
        return offers_by_user

    # This method uses current user for creating new offer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
