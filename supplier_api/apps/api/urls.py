# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from suppliers.views import (
    BaseSupplierViewSet, BaseRepresentationOrderViewSet, BaseDefendantViewSet)


router = routers.DefaultRouter()
router.register(r'suppliers', BaseSupplierViewSet, base_name='suppliers')
router.register(r'reporders', BaseRepresentationOrderViewSet, base_name='reporders')
router.register(r'defendants', BaseDefendantViewSet, base_name='defendants')

schema_view = get_swagger_view(
    title='Claim for crown court defence Supplier API - v1')

urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^docs/$', schema_view)
)
