from rest_framework.serializers import ValidationError
import collections


class StartEndDateValidator(object):
    def __init__(self, start_date_field, end_date_field, message=None):
        self.start = start_date_field
        self.end = end_date_field
        self.message = message

    def __call__(self, data):
        start = data.get(self.start)
        end = data.get(self.end)
        msg = self.message or "Start date must happen before end date"
        if all([start, end]):
            if start > end:
                raise ValidationError(msg)


class NotEmptyCollectionValidator(object):
    def __init__(self, collection_attribute):
        self.collection = collection_attribute

    def __call__(self, data):
        collection = data.get(self.collection)
        if collection is None or not isinstance(collection, collections.Iterable):
            raise ValidationError(self.collection + " must be an iterable object")
        if len(collection) == 0:
            raise ValidationError(self.collection + " must contain at least one item")
