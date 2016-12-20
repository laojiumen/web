# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=10, default="")

    def __unicode__(self):
        return self.label


class BigGod(models.Model):
    name = models.CharField(max_length=10, default="")
    english_name = models.CharField(max_length=10, default="")
    birthday = models.DateField()
    image = models.ImageField(upload_to="persons")
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.name
