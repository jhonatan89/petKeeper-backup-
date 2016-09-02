from __future__ import unicode_literals
from django.contrib import admin
from .models import Breed, Size, Offer, Pet, Request, Contact


admin.site.register(Breed)
admin.site.register(Size)
admin.site.register(Offer)
admin.site.register(Pet)
admin.site.register(Request)
admin.site.register(Contact)