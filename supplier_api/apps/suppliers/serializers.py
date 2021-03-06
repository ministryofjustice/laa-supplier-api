# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Supplier, RepresentationOrder, Defendant


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'code', 'parent', 'name', 'suty_supplier_type', 'vat_reg',
            'address', 'country'
        )


class DefendantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defendant
        fields = (
            'code', 'first_name', 'other_name', 'last_name', 'date_of_birth'
        )


class RepresentationOrderSerializer(serializers.ModelSerializer):
    defendant = DefendantSerializer(read_only=True)

    class Meta:
        model = RepresentationOrder
        fields = (
            'code', 'defendant', 'supplier', 'date'
        )
