""" petkeeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Django
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

# Django Rest Framework
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

# Views
from api.views import RequestViewSet, OfferViewSet
from api.views import PetViewSet
from api.views import SizeViewSet
from api.views import BreedViewSet


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

# Routers for request/{pk}/offers/{pk}
router = NestedDefaultRouter()
(
    router.register(r'requests', RequestViewSet, 'request').register(
                    r'offers', OfferViewSet, 'request-offer', parents_query_lookups=['request'])
)
# Routers provide an easy way of automatically determining the URL conf.
router.register(r'pets', PetViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'breeds', BreedViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]
