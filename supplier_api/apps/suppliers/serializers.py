# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Supplier, RepresentationOrder, Defendant


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'code',
        )


class RepresentationOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepresentationOrder
        fields = (
            'date',
        )


class DefendantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defendant
        fields = (
            'first_name',
            'last_name',
        )
