from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Credentials(models.Model):
    name = models.CharField(default="" ,max_length=50)
    password = models.CharField(max_length=20)
    isadmin = models.BooleanField(default="False")
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
