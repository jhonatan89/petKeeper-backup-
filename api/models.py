from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Request(models.Model):
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    open = models.BooleanField(default=False)
