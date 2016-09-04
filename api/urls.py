# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from api.views import (RequestViewSet, OfferViewSet, UserViewSet, PetViewSet, SizeViewSet, BreedViewSet, MeView,
                       PetRequestViewSet)


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

router.register(r'requests', RequestViewSet, 'request').register(
    r'offers', OfferViewSet, 'request-offer', parents_query_lookups=['request'])

router.register(r'requests', RequestViewSet, 'request').register(
    r'pets', PetRequestViewSet, 'request-pet', parents_query_lookups=['request'])


# Routers provide an easy way of automatically determining the URL conf.
router.register(r'pets', PetViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'profiles', UserViewSet)

urlpatterns = [
    url(r'^me/$', view=MeView.as_view(), name='me')
]

urlpatterns += router.urls
