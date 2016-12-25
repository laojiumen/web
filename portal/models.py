# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
from django.utils.html import format_html


@python_2_unicode_compatible
class Tag(models.Model):
    label = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class BigGod(models.Model):
    name = models.CharField(u"大神", max_length=10, default="")
    english_name = models.CharField(max_length=10, default="")
    birthday = models.DateField()
    image = models.ImageField(upload_to="persons")
    tags = models.ManyToManyField(Tag)

    def name2(self):
        return format_html(
            '<span style="color: red">{}</span>',
            self.name,
        )

    name2.admin_order_field = 'name'
    name2.short_description = u'全名2'

    def is_staff(self):
        return True

    def __str__(self):
        return self.name
