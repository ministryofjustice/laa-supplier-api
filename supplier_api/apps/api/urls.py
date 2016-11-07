# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_swagger.views import get_swagger_view

from suppliers.views import (
    BaseSupplierViewSet, BaseRepresentationOrderViewSet, BaseDefendantViewSet)


router = ExtendedSimpleRouter()
(
    router.register(r'suppliers', BaseSupplierViewSet, base_name='suppliers')
          .register(r'reporders',
                    BaseRepresentationOrderViewSet,
                    base_name='suppliers-reporders',
                    parents_query_lookups=['supplier__code'])
          .register(r'defendants',
                    BaseDefendantViewSet,
                    base_name='suppliers-reporders-defendants',
                    parents_query_lookups=['reporders__supplier__code',
                                           'reporders__code'])
)

schema_view = get_swagger_view(
    title='Claim for crown court defence Supplier API - v1')

urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^docs/$', schema_view)
)
