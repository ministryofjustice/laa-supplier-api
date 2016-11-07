# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Supplier, RepresentationOrder, Defendant
from .serializers import (SupplierSerializer, RepresentationOrderSerializer,
                          DefendantSerializer)


class AllObjectMixin():
    """
    Mixin to return all objects in the queryset
    """
    def get_queryset(self):
        return self.model.objects.all()


class BaseSupplierViewSet(
    NestedViewSetMixin, AllObjectMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows suppliers to be viewed.

    retrieve:
    Return a supplier instance.

    list:
    Return all suppliers, ordered by id
    """
    model = Supplier
    serializer_class = SupplierSerializer
    lookup_field = 'code'


class BaseRepresentationOrderViewSet(
    NestedViewSetMixin, AllObjectMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows rep orders to be viewed.

    retrieve:
    Return a rep order instance.

    list:
    Return all rep orders, ordered by id
    """
    model = RepresentationOrder
    serializer_class = RepresentationOrderSerializer
    lookup_field = 'code'


class BaseDefendantViewSet(
    NestedViewSetMixin, AllObjectMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows defendant to be viewed.

    retrieve:
    Return a defendant instance.

    list:
    Return all defendants, ordered by id
    """
    model = Defendant
    serializer_class = DefendantSerializer
    lookup_field = 'code'
