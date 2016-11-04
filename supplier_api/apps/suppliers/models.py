# -*- coding: utf-8 -*-
from django.db import models

from .constants import SUTY_SUPPLIER_TYPES


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Supplier(TimeStampedModel):
    parent = models.ForeignKey(
        'Supplier', related_name='children', null=True, blank=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, db_index=True)
    suty_supplier_type = models.PositiveSmallIntegerField(
        choices=SUTY_SUPPLIER_TYPES)
    vat_reg = models.BooleanField()
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=20)


class Defendant(TimeStampedModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()


class RepresentationOrder(TimeStampedModel):
    code = models.PositiveSmallIntegerField(db_index=True)
    defendant = models.ForeignKey('Defendant', related_name='reporders')
    supplier = models.ForeignKey('Supplier', related_name='reporders')
    date = models.DateField()
