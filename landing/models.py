# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class ListClient(models.Model):
    email = models.CharField(max_length=40)
    registrationDate = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return '%s' % self.email
