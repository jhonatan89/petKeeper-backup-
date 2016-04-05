from django.contrib import admin
from .models import Breed, Size, Offer, Pet, Request
# Register your models here.

admin.site.register(Breed)
admin.site.register(Size)
admin.site.register(Offer)
admin.site.register(Pet)
admin.site.register(Request)