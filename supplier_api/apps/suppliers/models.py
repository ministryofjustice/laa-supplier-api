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
    code = models.CharField(max_length=10, unique=True, db_index=True)
    parent = models.ForeignKey(
        'Supplier', related_name='children', null=True, blank=True)
    name = models.CharField(max_length=100)
    suty_supplier_type = models.PositiveSmallIntegerField(
        choices=SUTY_SUPPLIER_TYPES)
    vat_reg = models.BooleanField()
    address = models.TextField()
    postcode = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)


class Defendant(TimeStampedModel):
    code = models.PositiveIntegerField(unique=True, db_index=True)
    first_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()


class RepresentationOrder(TimeStampedModel):
    code = models.PositiveIntegerField(db_index=True, unique=True)
    defendant = models.ForeignKey('Defendant', related_name='reporders')
    supplier = models.ForeignKey('Supplier', related_name='reporders')
    date = models.DateField()
