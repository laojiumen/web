from __future__ import unicode_literals

from django.db import models


# Create your models here.

class BigGod(models.Model):
    name = models.CharField(max_length=10)
    birthday = models.DateField()
    image = models.ImageField(upload_to="persons")
    description = models.TextField()
    github = models.URLField()
