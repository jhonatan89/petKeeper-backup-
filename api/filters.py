# -*- coding: utf-8 -*-

import django_filters
from django.db.models import Count
from rest_framework import filters

from api.models import Request, Breed, Size


class RequestFilter(filters.FilterSet):
    start_date = django_filters.DateFilter(lookup_type='gte')  # Minimum start date
    end_date = django_filters.DateFilter(lookup_type='lte')  # Maximum end date
    breed = django_filters.ModelMultipleChoiceFilter(name='pets__breed', queryset=Breed.objects.all())  # Desired breeds
    size = django_filters.ModelMultipleChoiceFilter(name='pets__size', queryset=Size.objects.all())  # Desired sizes
    max = django_filters.MethodFilter()  # Maximum amount of pets to take care of

    def filter_max(self, queryset, value):
        return queryset.annotate(pet_count=Count('pets')).filter(pet_count__lte=value)

    class Meta:
        model = Request
        fields = ['start_date', 'end_date', 'breed', 'size', 'max']
