#Selializers
from api.model_serializers import RequestSerializer, BreedSerializer
from api.model_serializers import PetSerializer, OfferSerializer
from api.model_serializers import SizeSerializer

#Models
from api.models import Request, Breed, Offer
from api.models import Pet
from api.models import Size

#Django Rest Framework
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    # This method provide url_path='request/me'
    @list_route(methods=['get'], url_path='me')
    def me(self, request, pk=None):
        return Response({})

    # This method provide url_path='requests/{pk}/offers'
    @detail_route(methods=['get', 'post'], url_path='offers')
    def offers(self, request, pk=None):
        req = Request.objects.get(pk=pk)
        if request.method == 'GET':
            queryset = Offer.objects.filter(request=req)
            serializer_class = OfferSerializer(queryset, many=True, context={'request': request})
            return Response(serializer_class.data)
        if request.method == 'POST':
            serializer_class = OfferSerializer(data=request.data, context={'request': request})
            if serializer_class.is_valid():
                serializer_class.save(user=self.request.user, request=req)
                return Response(serializer_class.data, status=status.HTTP_201_CREATED)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


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
