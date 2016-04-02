#Selializers
from api.model_serializers import RequestSerializer, BreedSerializer
from api.model_serializers import PetSerializer
from api.model_serializers import SizeSerializer

#Models
from api.models import Request, Breed
from api.models import Pet
from api.models import Size

#Django Rest Framework
from rest_framework import viewsets

class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class PetViewSet(viewsets.ModelViewSet):

    queryset =  Pet.objects.all()
    serializer_class = PetSerializer

class SizeViewSet(viewsets.ModelViewSet):

    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class BreedViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all().order_by('name')
    serializer_class = BreedSerializer