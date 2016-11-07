# -*- coding: utf-8 -*-
from rest_framework import viewsets

from .models import Supplier, RepresentationOrder, Defendant
from .serializers import (SupplierSerializer, RepresentationOrderSerializer,
                          DefendantSerializer)


class AllObjectMixin():
    """
    Mixin to return all objects in the queryset
    """
    def get_queryset(self):
        return self.model.objects.all()


class BaseSupplierViewSet(AllObjectMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows suppliers to be viewed.

    retrieve:
    Return a supplier instance.

    list:
    Return all supplier, ordered by id
    """
    model = Supplier
    serializer_class = SupplierSerializer


class BaseRepresentationOrderViewSet(AllObjectMixin,
                                     viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows rep orders to be viewed.

    retrieve:
    Return a rep order instance.

    list:
    Return all rep order, ordered by id
    """
    model = RepresentationOrder
    serializer_class = RepresentationOrderSerializer


class BaseDefendantViewSet(AllObjectMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows defendant to be viewed.

    retrieve:
    Return a defendant instance.

    list:
    Return all defendant, ordered by id
    """
    model = Defendant
    serializer_class = DefendantSerializer
